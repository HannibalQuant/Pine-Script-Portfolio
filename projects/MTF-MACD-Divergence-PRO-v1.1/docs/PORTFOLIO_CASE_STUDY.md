# Case Study — MTF MACD Divergence PRO v1.1

## Brief

Build a professional TradingView indicator that detects MACD divergence across multiple timeframes without relying on future information.

## Main engineering risks

### 1. Higher-timeframe repainting
Naive MTF code can consume a still-developing higher-timeframe value.

**Response:** requested values are offset to the previous closed requested bar before they are exposed through `request.security()`.

### 2. Divergence pairing ambiguity
A divergence engine must define which oscillator swing belongs to which price swing.

**Response:** oscillator-pivot anchored pairing. Price is sampled on the same confirmed pivot bar.

### 3. Premature pivots
A pivot cannot be known before right-side confirmation bars exist.

**Response:** signals are emitted only after the configured `rightBars` confirmation delay.

### 4. MTF events rarely align on one chart bar
1H, 4H and 1D confirmations can arrive at different times.

**Response:** a configurable confirmation window counts recent evidence instead of forcing exact same-bar synchronization.

### 5. Static timeframe configuration broke when the chart moved higher
The v1.0 build intentionally rejected lower-than-chart requests, so a static 1H/4H/1D stack could stop when the chart was switched to 4H or 1D.

**Response in v1.1:** adaptive Auto mode. TF1 follows the chart, while TF2/TF3 resolve upward through a standard timeframe ladder. Manual mode keeps the fail-closed safety rule.

## Deliverables

- Pine Script v6 source
- regular + hidden bullish/bearish divergence
- adaptive 3-timeframe resolver
- MTF dashboard and consensus logic
- alert conditions and optional JSON payloads
- Python reference logic
- automated tests
- TradingView runtime evidence

## Validation status

- Pine v6 compile/runtime: **passed**
- adaptive timeframe switching: **passed**
- automated reference/static tests: **included**
- formal realtime HTF-close repaint observation: **pending**
- alert delivery test: **pending**

The project intentionally distinguishes verified behavior from checks that have not yet been completed.
