# MTF Stochastics PRO v1

Portfolio-grade **Pine Script v6** indicator for adaptive multi-timeframe Stochastic analysis.

## What it demonstrates

- Pine Script v6
- adaptive `request.security()` architecture
- Stochastic %K / %D
- overbought / oversold reversal crosses
- midline momentum events
- optional %K/%D alignment filter
- Auto / Manual timeframe modes
- MTF consensus window
- dashboard
- alert conditions
- JSON alerts
- Python reference logic
- automated tests
- explicit non-repainting HTF request contract

## Signal families

### Reversal
- bullish: %K crosses above %D while the pair reaches the oversold region
- bearish: %K crosses below %D while the pair reaches the overbought region

### Momentum
- bullish: %K crosses above the momentum midline
- bearish: %K crosses below the momentum midline
- optional %K/%D directional alignment

The MTF consensus engine can use `Reversal`, `Momentum`, or `Either`.

## Adaptive timeframe mode

Auto mode is the default.

| Chart | TF1 | TF2 | TF3 |
|---|---|---|---|
| 15m | 15m | 1H | 4H |
| 1H | 1H | 4H | 1D |
| 2H | 2H | 4H | 1D |
| 4H | 4H | 1D | 1W |
| 1D | 1D | 1W | 1M |

Manual mode is available but deliberately rejects lower-than-chart requests.

## Non-repainting contract

Requested-timeframe values are returned from the previous fully closed requested bar:

```pine
[br[1], sr[1], bm[1], sm[1], k[1], d[1], time[1]]
```

and requested with:

```pine
lookahead = barmerge.lookahead_on
```

This intentionally favors stable confirmed data over premature signals.

## Source

- `pine/MTF_Stochastics_PRO_v1.pine`
- `python_ref/`
- `tests/`
- `docs/NON_REPAINTING.md`
- `docs/PORTFOLIO_CASE_STUDY.md`

## Status

**Source package + automated validation: complete.**

**TradingView runtime verification: pending manual platform pass.**

This project is an engineering demonstration, not a profitability claim or financial advice.
