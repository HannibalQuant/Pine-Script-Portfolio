# MTF MACD Divergence PRO v1.1

Portfolio-grade **Pine Script v6** indicator for adaptive multi-timeframe MACD divergence detection.

![TradingView runtime](assets/runtime_evidence/04_v1_1_auto_mtf_xagusd_4h.png)

## What it demonstrates

- Pine Script v6
- `request.security()` and multi-timeframe architecture
- regular + hidden bullish/bearish MACD divergence
- confirmed pivot detection
- adaptive Auto timeframe mode
- confirmed higher-timeframe values using an explicit `[1]` offset
- `barmerge.lookahead_on` used only with already-confirmed requested-timeframe data
- MTF consensus window and dashboard
- alert conditions + optional JSON alerts
- defensive input validation
- Python reference implementation
- automated regression tests

## Adaptive timeframe mode

Auto mode is the default. TF1 follows the active chart and TF2/TF3 move upward through a standard timeframe ladder.

| Chart | TF1 | TF2 | TF3 |
|---|---|---|---|
| 15m | 15m | 1H | 4H |
| 1H | 1H | 4H | 1D |
| 2H | 2H | 4H | 1D |
| 4H | 4H | 1D | 1W |
| 1D | 1D | 1W | 1M |
| 1W | 1W | 1M | 3M |

Manual mode remains available and deliberately fails closed if a requested timeframe is below the chart timeframe.

## Divergence rules

- Regular bullish: lower price low + higher MACD low
- Regular bearish: higher price high + lower MACD high
- Hidden bullish: higher price low + lower MACD low
- Hidden bearish: lower price high + higher MACD high

The oscillator pivot is the pairing anchor. Price is sampled on the same confirmed pivot bar.

## Runtime status

**TradingView runtime: PASSED — 2026-10-01.**

The v1.1 build was tested while switching across multiple chart intervals. The adaptive MTF resolver stayed operational and removed the v1.0 lower-timeframe guard failure in Auto mode.

Automated tests cover divergence classification, pivot confirmation delay, timeframe resolution, Pine source contracts, and parser regressions.

## Source

- [`pine/MTF_MACD_Divergence_PRO_v1_1.pine`](pine/MTF_MACD_Divergence_PRO_v1_1.pine)
- [`python_ref/`](python_ref/)
- [`tests/`](tests/)
- [`docs/NON_REPAINTING.md`](docs/NON_REPAINTING.md)
- [`docs/PORTFOLIO_CASE_STUDY.md`](docs/PORTFOLIO_CASE_STUDY.md)

## Validation boundary

Runtime compatibility has been verified. A formal realtime observation across an HTF close and alert-delivery verification remain separate checks; this repository does not overstate them as completed.

This project is an engineering demonstration, not a profitability claim or financial advice.
