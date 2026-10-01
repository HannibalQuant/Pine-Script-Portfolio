# MTF Stochastics PRO v1

Portfolio-grade **Pine Script v6** indicator for adaptive multi-timeframe Stochastic analysis.

## What it demonstrates

- adaptive multi-timeframe Stochastic %K / %D
- overbought / oversold reversal logic
- midline momentum events
- optional %K/%D directional alignment
- Auto / Manual timeframe modes
- MTF consensus window
- dashboard
- alert conditions and JSON alerts
- confirmed requested-timeframe data
- explicit non-repainting HTF design

## Signal families

### Reversal
- bullish: %K crosses above %D while the pair reaches the oversold region
- bearish: %K crosses below %D while the pair reaches the overbought region

### Momentum
- bullish: %K crosses above the configured momentum midline
- bearish: %K crosses below the configured momentum midline
- optional %K/%D directional alignment

The MTF consensus engine can use `Reversal`, `Momentum`, or `Either`.

## Runtime status

**TradingView runtime: PASSED — BTCUSDT 1H.**

The indicator rendered %K/%D, MTF BULL / MTF BEAR labels, Auto timeframe state, and dashboard values without a runtime error.

## Validation summary

Private automated validation covers oscillator calculations, reversal / momentum classification, timeframe resolution, Pine source contracts, and parser regressions.

## Public code excerpt

A limited architecture excerpt is available in [`PUBLIC_CODE_EXCERPT.md`](PUBLIC_CODE_EXCERPT.md). It is intentionally incomplete and does not contain the proprietary signal engine.

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- [`docs/NON_REPAINTING.md`](docs/NON_REPAINTING.md)
- [`docs/PORTFOLIO_CASE_STUDY.md`](docs/PORTFOLIO_CASE_STUDY.md)
- [`docs/RUNTIME_VALIDATION.md`](docs/RUNTIME_VALIDATION.md)
- [`CHANGELOG.md`](CHANGELOG.md)

## Source availability

The complete Pine Script implementation and private validation code are **not public**. They are available for controlled review with serious clients when appropriate.

This project is an engineering demonstration, not a profitability claim or financial advice.
