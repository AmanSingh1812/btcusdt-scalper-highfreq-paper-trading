# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

_Simulator only. No real money, no exchange account, no API keys. 5-minute bars, zone 0.8% of level, score>=1/6, tight 1.5R/2.5R partials, hard 48-bar (240 min) time-stop, 50% position sizing - widened from ../scalper bot (0.2% zone, score>=3) for ~2.5x trade frequency. See README. Last updated: 2026-10-14T13:06:01.877702+00:00_

## Current State

- Equity: **99.98 USDT** (started at 100.00)
- Last processed bar: 2026-10-14 13:00:00+00:00
- Position: **SHORT** 0.000599 BTC @ 83477.98 (SL 84146.77, TP1 82474.85, TP2 81806.07, TP1 filled: False)
- Signal(s) this run: ['SELL score 1/6 @ 83478.00 (2026-10-14T09:10:00.000000)']

## Genuine Live Stats (since deployment)

No trades yet since deployment - equity is exactly the $100 starting balance.


## Backtest reference (not live balance)

Full 9.14-year backtest at 50% sizing: 3501 trades (0.96/day), 66.92% win rate, PF 2.166, CAGR 21.17%/yr, max DD -3.56%. Every calendar year 2017-2026 was profitable. See README for the comparison against ../scalper bot's lower-frequency config. The deployment starts clean at $100 - this backtest record is not replayed into the live balance.
