# Architecture

## Pipeline

1. Resolve chart / higher timeframes in Auto mode, or validate Manual mode.
2. Compute raw Stochastic %K inside the requested timeframe.
3. Smooth %K and derive %D.
4. Classify reversal and momentum events.
5. Shift the complete requested payload by one requested-timeframe bar.
6. Pull the pack with `request.security(..., lookahead_on)`.
7. Convert held HTF booleans into one-chart-bar pulses.
8. Count recent bullish / bearish evidence in the MTF confirmation window.
9. Render oscillator, dashboard, signal markers and alerts.

## Event design

Reversal and momentum are intentionally separate signal families. This avoids mixing "leaving an extreme" with "crossing the oscillator center" into one opaque condition.

## Boundaries

This is an indicator, not a strategy. It does not:
- place orders
- simulate fills
- optimize parameters
- connect to a broker
- claim profitability
