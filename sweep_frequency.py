"""
Sweep near-zone width and score threshold to find configs that trade more
often than ../scalper bot's ~0.4 trades/day, and check the cost. Run
against the full available history for a robust read (not a short window).
"""
import pandas as pd

import scalper_engine as se

CONFIGS = [
    (0.2, 3, "baseline (../scalper bot)"),
    (0.3, 3, "wider zone 0.3%, score>=3"),
    (0.4, 3, "wider zone 0.4%, score>=3"),
    (0.2, 2, "baseline zone, score>=2"),
    (0.3, 2, "wider zone 0.3%, score>=2"),
    (0.4, 2, "wider zone 0.4%, score>=2"),
    (0.5, 2, "zone=0.5%, score>=2"),
    (0.6, 2, "zone=0.6%, score>=2"),
    (0.4, 1, "zone=0.4%, score>=1"),
    (0.5, 1, "zone=0.5%, score>=1"),
    (0.6, 1, "zone=0.6%, score>=1"),
    (0.8, 1, "zone=0.8%, score>=1 (deployed here)"),
]


def main():
    df = pd.read_parquet("data/btcusdt_5m.parquet").sort_values("open_time").reset_index(drop=True)
    for zone_pct, score_threshold, label in CONFIGS:
        dfi = se.compute_indicators(df.copy(), zone_pct=zone_pct)
        se.QTY_PCT_OF_EQUITY = 0.50
        trades, final_equity = se.run_backtest(dfi, score_threshold=score_threshold, rr1=se.RR1, rr2=se.RR2,
                                                 tp2_enabled=se.TP2_ENABLED, use_htf_filter=True,
                                                 enable_breakout_protection=True, max_hold_bars=se.MAX_HOLD_BARS)
        tdf = pd.DataFrame(trades)
        wins, losses = tdf[tdf.pnl > 0], tdf[tdf.pnl <= 0]
        pf = wins["pnl"].sum() / -losses["pnl"].sum() if losses["pnl"].sum() != 0 else float("inf")
        eq_curve = se.INITIAL_CAPITAL + tdf.sort_values("exit_time")["pnl"].cumsum()
        max_dd = ((eq_curve - eq_curve.cummax()) / eq_curve.cummax()).min() * 100
        span_days = (pd.to_datetime(tdf["exit_time"].iloc[-1]) - pd.to_datetime(tdf["entry_time"].iloc[0])).days
        years = span_days / 365.25
        cagr = ((final_equity / se.INITIAL_CAPITAL) ** (1 / years) - 1) * 100 if final_equity > 0 else float("-inf")
        print(f"{label}: trades={len(tdf)} trades/day={len(tdf)/span_days:.2f} "
              f"win%={100*(tdf.pnl>0).mean():.1f} PF={pf:.3f} CAGR={cagr:.2f}% maxDD={max_dd:.2f}%")


if __name__ == "__main__":
    main()
