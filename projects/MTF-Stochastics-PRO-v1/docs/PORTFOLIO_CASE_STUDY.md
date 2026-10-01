# Portfolio Case Study — MTF Stochastics PRO v1

## Brief

Build a professional multi-timeframe Stochastic indicator that demonstrates confirmed-bar logic, adaptive timeframe handling, alerts and a clean client-facing dashboard.

## Engineering problems addressed

### 1. Static timeframe fragility

Hard-coded lower timeframe inputs can break when the chart interval is increased.

**Response:** Auto mode follows the chart and resolves TF2 / TF3 upward.

### 2. HTF repainting

Developing higher-timeframe oscillator values can differ after reload.

**Response:** previous requested-bar offset + `lookahead_on`.

### 3. Signal ambiguity

A Stochastic cross in an extreme zone is not the same event as a centerline momentum transition.

**Response:** separate Reversal and Momentum signal families, plus selectable MTF consensus mode.

### 4. MTF timing mismatch

Signals across timeframes rarely occur on the same chart bar.

**Response:** configurable confirmation window and minimum timeframe count.

## Deliverables

- Pine Script v6 indicator
- adaptive MTF resolver
- reversal + momentum engine
- dashboard
- alert conditions
- JSON alerts
- Python reference
- automated tests
- runtime acceptance checklist

## Status

Engineering package: **complete**

Automated validation: **complete**

TradingView runtime evidence: **pending**
