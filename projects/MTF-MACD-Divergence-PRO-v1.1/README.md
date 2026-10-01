# MTF MACD Divergence PRO v1.1

Portfolio-grade **Pine Script v6** indicator for adaptive multi-timeframe MACD divergence detection.

## What it demonstrates

- regular + hidden bullish / bearish MACD divergence
- oscillator-pivot swing pairing
- adaptive Auto / Manual timeframe modes
- confirmed higher-timeframe values
- MTF confirmation window and dashboard
- alert conditions and JSON alerts
- defensive validation
- explicit no-lookahead / non-repainting design

## Adaptive timeframe mode

Auto mode follows the active chart timeframe and resolves TF2 / TF3 upward through a standard timeframe ladder.

Examples:

| Chart | TF1 | TF2 | TF3 |
|---|---|---|---|
| 15m | 15m | 1H | 4H |
| 1H | 1H | 4H | 1D |
| 2H | 2H | 4H | 1D |
| 4H | 4H | 1D | 1W |
| 1D | 1D | 1W | 1M |

Manual mode remains available and deliberately rejects lower-than-chart requests.

## Runtime status

**TradingView runtime: PASSED.**

The adaptive v1.1 build was tested across multiple chart intervals and remained operational after the v1.0 static-timeframe limitation was corrected.

## Validation summary

Private automated validation covers divergence classification, pivot confirmation delay, timeframe resolution, Pine source contracts, and parser regressions.

## Public code excerpt

A limited architecture excerpt is available in [`PUBLIC_CODE_EXCERPT.md`](PUBLIC_CODE_EXCERPT.md). It is intentionally incomplete and does not contain the proprietary signal engine.

## Documentation

- [`docs/NON_REPAINTING.md`](docs/NON_REPAINTING.md)
- [`docs/PORTFOLIO_CASE_STUDY.md`](docs/PORTFOLIO_CASE_STUDY.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Source availability

The complete Pine Script implementation and private validation code are **not public**. They are available for controlled review with serious clients when appropriate.

This project is an engineering demonstration, not a profitability claim or financial advice.
