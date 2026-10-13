# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

A sibling of [`../scalper bot`](../scalper%20bot) — same engine, same 5m
PDH/PDL confluence signal with tight R:R and a hard time-stop, but with
the entry criteria widened to trade roughly **2.5x more often**, because
the original config averages only ~0.4 trades/day (see that repo's
history for why "at least one trade a day" turned out to be a higher bar
than the original strategy was ever validated at).

## What's different from `../scalper bot`

| | Original | This (high-frequency) |
|---|---|---|
| Near-zone | 0.2% of level | **0.8%** of level |
| Score threshold | >=3/6 | **>=1/6** |
| Everything else | identical | identical |

## Backtest, full available history (2017-08 to present, 9.14 years)

| Config | Trades | Trades/day | Win rate | PF | CAGR | Max DD |
|---|---|---|---|---|---|---|
| Original (zone 0.2%, score>=3) | 1362 | 0.41 | 71.07% | 2.965 | 13.52%/yr | -3.13% |
| **This (zone 0.8%, score>=1)** | **3501** | **0.96** | **66.92%** | **2.166** | **21.17%/yr** | **-3.56%** |

Loosening the criteria trades some win rate (71%→67%) and profit factor
(2.97→2.17) for roughly 2.5x the trade frequency - but CAGR is actually
*higher*, not lower, because the extra volume of still-solidly-positive
trades compounds faster than the slightly lower per-trade quality costs.
Max drawdown barely moved (-3.13%→-3.56%). Every single calendar year
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
