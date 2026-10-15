# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

_Simulator only. No real money, no exchange account, no API keys. 5-minute bars, zone 0.8% of level, score>=1/6, tight 1.5R/2.5R partials, hard 48-bar (240 min) time-stop, 50% position sizing - widened from ../scalper bot (0.2% zone, score>=3) for ~2.5x trade frequency. See README. Last updated: 2026-10-15T04:37:54.576398+00:00_

## Current State

- Equity: **100.58 USDT** (started at 100.00)
- Last processed bar: 2026-10-15 04:30:00+00:00
- Position: **flat**

## Genuine Live Stats (since deployment)

- Total trades: 2
- Win rate: 100.00%
- Total PnL: 0.58 USDT (0.58%)
- Profit factor: inf
- CAGR: 78.39%/year
- Max drawdown: 0.00%

## Most Recent Trades

| Entry time | Side | Exit reason | Entry | Exit | Bars held | PnL |
|---|---|---|---|---|---|---|
| 2026-10-14 09:10:00 | short | TIME | 83477.98 | 82410.12 | 49 | 0.30 |
| 2026-10-14 09:10:00 | short | TP1 | 83477.98 | 82474.85 | 48 | 0.28 |

## Backtest reference (not live balance)

Full 9.14-year backtest at 50% sizing: 3501 trades (0.96/day), 66.92% win rate, PF 2.166, CAGR 21.17%/yr, max DD -3.56%. Every calendar year 2017-2026 was profitable. See README for the comparison against ../scalper bot's lower-frequency config. The deployment starts clean at $100 - this backtest record is not replayed into the live balance.
