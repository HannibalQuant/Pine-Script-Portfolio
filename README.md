# Pine Script Portfolio

Professional **Pine Script v6** portfolio focused on multi-timeframe logic, confirmed-bar execution, non-repainting design, alerts, and TradingView runtime validation.

> **Closed-source portfolio:** the complete Pine Script source code and private validation implementations are intentionally not published in this repository. They are available for controlled review with serious clients when appropriate.

## Featured projects

### 1. MTF MACD Divergence PRO v1.1

Adaptive multi-timeframe MACD divergence indicator featuring regular and hidden bullish/bearish divergence, Auto / Manual timeframe modes, confirmed higher-timeframe data, MTF consensus, dashboard, alert conditions, and JSON alerts.

**TradingView runtime:** PASSED on multiple chart intervals.  
**Public materials:** architecture, case study, runtime notes, changelog, and a limited non-proprietary code excerpt.

[**Open MTF MACD Divergence PRO v1.1 →**](projects/MTF-MACD-Divergence-PRO-v1.1/README.md)

---

### 2. MTF Stochastics PRO v1

Adaptive multi-timeframe Stochastic oscillator featuring %K / %D analysis, overbought / oversold reversal logic, midline momentum events, Auto / Manual timeframes, MTF consensus, dashboard, alert conditions, and JSON alerts.

**TradingView runtime:** PASSED on BTCUSDT 1H.  
**Public materials:** architecture, case study, runtime notes, changelog, and a limited non-proprietary code excerpt.

[**Open MTF Stochastics PRO v1 →**](projects/MTF-Stochastics-PRO-v1/README.md)

## What this repository proves

- Pine Script v6 project design
- `request.security()` / multi-timeframe architecture
- confirmed-bar and no-lookahead semantics
- non-repainting HTF request patterns
- divergence and oscillator engineering
- alerts and webhook-ready JSON payloads
- defensive input validation
- documented runtime validation
- iterative debugging from observed TradingView behavior

## Source-code policy

The public repository is a **portfolio showcase**, not a source-code distribution repository.

The full `.pine` implementations, Python mirrors, and private regression suites are kept private to protect the intellectual property while still showing the engineering approach and verified runtime behavior.

See [SOURCE_POLICY.md](SOURCE_POLICY.md).

## TradingView demos

Protected TradingView publications will be linked here after publication. They will allow clients to evaluate the indicators without exposing the source code.

## Contact / client review

For a serious project discussion, full source can be reviewed in a controlled setting or through temporary private access when appropriate.

Portfolio projects are engineering demonstrations. They do not make profitability claims and are not financial advice.
