# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

A sibling of [`../scalper bot`](../scalper%20bot) — same engine, same 5m
PDH/PDL confluence signal with tight R:R and a hard time-stop, but with
the entry criteria widened to trade roughly **2.5x more often**, because
the original config averages only ~0.4 trades/day (see that repo's
history for why "at least one trade a day" turned out to be a higher bar
than the original strategy was ever validated at).

## ETH/XRP: tried, validated, reverted by request (not because they failed)

This repo briefly traded BTCUSDT, ETHUSDT, and XRPUSDT independently
(each its own $100 equity pool), inheriting `../scalper bot`'s
`scalper_engine.TICK_SIZES` fix (XRP's real Binance tick is 0.0001, not
0.01 - using the wrong one originally produced a fake "account
destroyed" backtest result). Full validated numbers (100% sizing, full
available history per symbol):

| Symbol | History | Trades | Trades/day | Win rate | PF | CAGR | Max DD |
|---|---|---|---|---|---|---|---|
| BTCUSDT | 9.1yr | 3509 | 1.05 | 66.9% | 2.10 | 46.56%/yr | -7.05% |
| ETHUSDT | 9.2yr | 2797 | 0.83 | 72.4% | 2.46 | 71.27%/yr | -8.58% |
| XRPUSDT | 8.4yr | 2470 | 0.80 | 73.8% | 2.22 | 65.34%/yr | -5.99% |

Same pattern as the lower-frequency original: the edge transferred
cleanly to both new symbols, with ETH and XRP actually showing *higher*
CAGR than BTC here. **Reverted back to BTC-only by request** - the
ETH/XRP data and live trade history were removed, but
`fetch_data.py`/`paper_trade.py` still loop over a `SYMBOLS` list
(currently just `["BTCUSDT"]`), so re-adding either symbol later is a
one-line change plus a re-fetch, not a rebuild.

## What's different from `../scalper bot`

| | Original | This (high-frequency) |
|---|---|---|
| Near-zone | 0.2% of level | **0.8%** of level |
| Score threshold | >=3/6 | **>=1/6** |
| Everything else | identical | identical |

## Backtest, BTCUSDT, full available history (2017-08 to present, 9.14 years)

| Config | Sizing | Trades | Trades/day | Win rate | PF | CAGR | Max DD |
|---|---|---|---|---|---|---|---|
| Original (zone 0.2%, score>=3) | 100% | 1362 | 0.41 | 71.07% | 2.742 | 28.64%/yr | -6.21% |
| **This (zone 0.8%, score>=1)** | 100% | **3509** | **1.05** | **66.9%** | **2.097** | **46.56%/yr** | **-7.05%** |

Loosening the criteria trades some win rate (71%→67%) and profit factor
(2.74→2.10) for roughly 2.5x the trade frequency - but CAGR is actually
*higher*, not lower, because the extra volume of still-solidly-positive
trades compounds faster than the slightly lower per-trade quality costs.
Max drawdown barely moved (-6.21%→-7.05%). Every single calendar year
2017-2026 was profitable (year PF ranged 1.67-2.88) at this looser
config too - same robustness check as the original.

A broader sweep (`sweep_frequency.py`) was run first to find this point -
intermediate configs (zone 0.3-0.6%, score>=1-2) sit between the two rows
above, all still solidly profitable; this repo deploys the config that
first crossed an average of 1 trade/day.

**Honest caveat carried over from the original**: "0.96 trades/day" is
still an *average* over a naturally bursty process (trades cluster when
a level gets tested repeatedly, then go quiet) - not a guarantee of
literally one trade every single calendar day without exception.

## How it works

Identical architecture to `../scalper bot` - see that repo's README for
the full v1 (failed oscillator scalper) / v2 (fixed, adapted PDH/PDL
signal) investigation, which this config inherits unchanged. Only the
zone/threshold parameters differ.

```bash
pip install -r requirements.txt
python fetch_data.py        # full history, or pass years-back e.g. `python fetch_data.py 2`
python backtest.py          # full-history backtest report
python paper_trade.py       # one live-trading cycle
```

No API keys or secrets needed anywhere in this repo.

## Disclaimer

This is a research/educational simulator. Past and simulated performance
is not indicative of future results. Nothing here is financial advice.
