# BTCUSDT Scalper (High-Frequency) — Live Paper Trading

_Simulator only. No real money, no exchange account, no API keys. 5-minute bars, zone 0.8% of level, score>=1/6, tight 1.5R/2.5R partials, hard 48-bar (240 min) time-stop, 50% position sizing - widened from ../scalper bot (0.2% zone, score>=3) for ~2.5x trade frequency. See README. Last updated: 2026-10-13T23:24:05.067218+00:00_

## Current State

- Equity: **100.00 USDT** (started at 100.00)
- Last processed bar: 2026-10-13 23:15:00+00:00
- Position: **flat**
- Signal(s) this run: (showing last 10 of 2241) ['BUY score 2/6 @ 84782.74 (2026-10-04T01:05:00.000000)', 'BUY score 3/6 @ 85398.01 (2026-10-05T18:05:00.000000)', 'BUY score 3/6 @ 85684.00 (2026-10-06T01:45:00.000000)', 'SELL score 3/6 @ 86560.67 (2026-10-06T15:05:00.000000)', 'SELL score 3/6 @ 83120.00 (2026-10-09T13:05:00.000000)', 'SELL score 4/6 @ 82820.01 (2026-10-10T06:45:00.000000)', 'BUY score 4/6 @ 83000.01 (2026-10-11T00:00:00.000000)', 'SELL score 2/6 @ 83046.00 (2026-10-11T03:05:00.000000)', 'BUY score 4/6 @ 83531.09 (2026-10-12T01:50:00.000000)', 'BUY score 3/6 @ 83460.15 (2026-10-12T09:25:00.000000)']

## Genuine Live Stats (since deployment)

No trades yet since deployment - equity is exactly the $100 starting balance.


## Backtest reference (not live balance)

Full 9.14-year backtest at 50% sizing: 3501 trades (0.96/day), 66.92% win rate, PF 2.166, CAGR 21.17%/yr, max DD -3.56%. Every calendar year 2017-2026 was profitable. See README for the comparison against ../scalper bot's lower-frequency config. The deployment starts clean at $100 - this backtest record is not replayed into the live balance.
