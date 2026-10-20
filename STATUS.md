# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

_Simulator only. No real money, no exchange account, no API keys. 5-minute bars, zone 0.8% of level, score>=1/6, tight 1.5R/2.5R partials, hard 48-bar (240 min) time-stop, 100% position sizing - widened from ../scalper bot (0.2% zone, score>=3) for ~2.5x trade frequency. See README. Last updated: 2026-10-20T22:08:06.498734+00:00_

## Current State

- Equity: **102.18 USDT** (started at 100.00)
- Last processed bar: 2026-10-20 22:00:00+00:00
- Position: **flat**

## Genuine Live Stats (since deployment)

- Total trades: 17
- Win rate: 76.47%
- Total PnL: 2.18 USDT (2.18%)
- Profit factor: 5.602
- CAGR: 271.97%/year
- Max drawdown: -0.31%

## Most Recent Trades

| Entry time | Side | Exit reason | Entry | Exit | Bars held | PnL |
|---|---|---|---|---|---|---|
| 2026-10-20 19:20:00 | long | TP2 | 82405.30 | 82625.20 | 5 | 0.10 |
| 2026-10-20 19:20:00 | long | TP1 | 82405.30 | 82537.23 | 4 | 0.04 |
| 2026-10-20 15:10:00 | long | TIME | 82418.22 | 82536.07 | 48 | 0.03 |
| 2026-10-20 15:10:00 | long | TP1 | 82418.22 | 82801.58 | 19 | 0.20 |
| 2026-10-20 03:05:00 | long | TIME | 81848.03 | 81783.56 | 48 | -0.16 |
| 2026-10-19 15:05:00 | short | TIME | 82269.99 | 81866.35 | 48 | 0.21 |
| 2026-10-19 15:05:00 | short | TP1 | 82269.99 | 81849.95 | 11 | 0.22 |
| 2026-10-18 22:15:00 | long | TIME | 81560.26 | 82432.70 | 48 | 0.50 |
| 2026-10-18 22:15:00 | long | TP1 | 81560.26 | 82541.29 | 47 | 0.56 |
| 2026-10-18 01:05:00 | long | TP2 | 81567.59 | 81879.45 | 8 | 0.08 |
| 2026-10-18 01:05:00 | long | TP1 | 81567.59 | 81754.70 | 7 | 0.04 |
| 2026-10-18 00:00:00 | short | SL | 81471.59 | 81523.74 | 11 | -0.07 |
| 2026-10-16 01:05:00 | short | SL | 82296.49 | 82466.47 | 2 | -0.14 |
| 2026-10-15 20:50:00 | long | SL | 82075.99 | 81985.70 | 1 | -0.10 |
| 2026-10-15 15:05:00 | long | TIME | 82200.06 | 82444.40 | 48 | 0.11 |

## Backtest reference (not live balance)

Full 9.14-year backtest at 100% sizing: 3501 trades (0.96/day), 66.92% win rate, PF 2.166, CAGR 21.17%/yr, max DD -3.56%. Every calendar year 2017-2026 was profitable. See README for the comparison against ../scalper bot's lower-frequency config. The deployment starts clean at $100 - this backtest record is not replayed into the live balance.
