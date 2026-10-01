# Changelog

## v1.1 — Adaptive MTF

### Fixed
- Switching the chart above a static 1H context no longer breaks the indicator in default Auto mode.
- Removed the hard dependency on a fixed 1H / 4H / 1D stack.

### Added
- Auto / Manual timeframe modes.
- TF1 follows the active chart in Auto mode.
- TF2/TF3 resolve automatically to higher standard timeframes.
- Dashboard exposes active mode and current chart context.
- JSON alerts include resolved TF1/TF2/TF3 values.
- Python reference model for the adaptive timeframe resolver.
- CI regression checks.

### Preserved
- confirmed requested-timeframe values
- `[1]` offset + `barmerge.lookahead_on` request contract
- manual lower-timeframe fail-closed guard
- regular/hidden bullish and bearish MACD divergence

### Runtime validation
- TradingView v1.1 runtime pass completed on 2026-10-01.
- Adaptive Auto mode confirmed working across tested chart intervals.
