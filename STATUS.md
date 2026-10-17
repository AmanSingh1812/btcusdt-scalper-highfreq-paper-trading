# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

_Simulator only. No real money, no exchange account, no API keys. 5-minute bars, zone 0.8% of level, score>=1/6, tight 1.5R/2.5R partials, hard 48-bar (240 min) time-stop, 50% position sizing - widened from ../scalper bot (0.2% zone, score>=3) for ~2.5x trade frequency. See README. Last updated: 2026-10-17T21:12:14.086594+00:00_

## Current State

- Equity: **100.45 USDT** (started at 100.00)
- Last processed bar: 2026-10-17 21:05:00+00:00
- Position: **flat**

## Genuine Live Stats (since deployment)

- Total trades: 5
- Win rate: 60.00%
- Total PnL: 0.45 USDT (0.45%)
- Profit factor: 2.876
- CAGR: 56.65%/year
- Max drawdown: -0.24%

## Most Recent Trades

| Entry time | Side | Exit reason | Entry | Exit | Bars held | PnL |
|---|---|---|---|---|---|---|
| 2026-10-16 01:05:00 | short | SL | 82296.49 | 82466.47 | 2 | -0.14 |
| 2026-10-15 20:50:00 | long | SL | 82075.99 | 81985.70 | 1 | -0.10 |
| 2026-10-15 15:05:00 | long | TIME | 82200.06 | 82444.40 | 48 | 0.11 |
| 2026-10-14 09:10:00 | short | TIME | 83477.98 | 82410.12 | 49 | 0.30 |
| 2026-10-14 09:10:00 | short | TP1 | 83477.98 | 82474.85 | 48 | 0.28 |

## Backtest reference (not live balance)

Full 9.14-year backtest at 50% sizing: 3501 trades (0.96/day), 66.92% win rate, PF 2.166, CAGR 21.17%/yr, max DD -3.56%. Every calendar year 2017-2026 was profitable. See README for the comparison against ../scalper bot's lower-frequency config. The deployment starts clean at $100 - this backtest record is not replayed into the live balance.
