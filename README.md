# Pine Script Portfolio

[![portfolio-tests](https://github.com/HannibalQuant/Pine-Script-Portfolio/actions/workflows/portfolio-tests.yml/badge.svg)](https://github.com/HannibalQuant/Pine-Script-Portfolio/actions/workflows/portfolio-tests.yml)

Professional **Pine Script v6** indicators and trading tools focused on multi-timeframe logic, confirmed-bar execution, non-repainting design, alerts, and Python validation.

## Featured projects

### 1. MTF MACD Divergence PRO v1.1

Adaptive multi-timeframe MACD divergence indicator featuring:

- regular + hidden bullish/bearish divergence
- Auto / Manual timeframe modes
- confirmed higher-timeframe data
- pivot-confirmed signals
- MTF consensus window and dashboard
- TradingView alert conditions
- optional JSON alert payloads
- Python reference logic
- automated GitHub Actions tests

**TradingView runtime:** passed on multiple chart intervals.  
**CI:** active and passing.

[**Open MTF MACD Divergence PRO v1.1 →**](projects/MTF-MACD-Divergence-PRO-v1.1/README.md)

---

### 2. MTF Stochastics PRO v1

Adaptive multi-timeframe Stochastic oscillator featuring:

- %K / %D analysis
- overbought / oversold reversal crosses
- midline momentum events
- optional %K/%D alignment filter
- Auto / Manual timeframe modes
- selectable MTF consensus family: Reversal / Momentum / Either
- confirmation window and dashboard
- TradingView alert conditions
- optional JSON alert payloads
- Python reference logic
- automated regression tests

**Source package:** complete.  
**Automated validation:** complete.  
**TradingView runtime:** pending manual platform pass.

[**Open MTF Stochastics PRO v1 →**](projects/MTF-Stochastics-PRO-v1/README.md)

## Engineering focus

- Pine Script v6
- `request.security()` / multi-timeframe architecture
- confirmed-bar and no-lookahead semantics
- non-repainting HTF request patterns
- divergence and oscillator logic
- alerts and webhook-ready JSON payloads
- defensive input validation
- Python reference implementations
- automated regression tests
- TradingView runtime verification

## Portfolio roadmap

| Project | Status |
|---|---|
| MTF MACD Divergence PRO v1.1 | **Available / runtime passed** |
| MTF Stochastics PRO v1 | **Available / runtime test pending** |
| Strategy / backtest portfolio example | Planned |

## About this repository

The goal is to show not only working Pine code, but the engineering around it: explicit execution semantics, validation boundaries, regression testing, runtime evidence, and clear documentation.

Portfolio projects are engineering demonstrations. They do not make profitability claims and are not financial advice.
