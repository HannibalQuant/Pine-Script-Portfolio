# Test Plan

## Automated

```bash
python -m pip install -r requirements.txt
pytest -q
```

Coverage includes:
- Stochastic output range
- bullish / bearish reversal signals
- bullish / bearish midline momentum
- alignment filter
- invalid-threshold rejection
- length mismatch rejection
- adaptive timeframe ladder
- Pine v6 contract
- confirmed `[1]` requested payload
- three `request.security()` calls
- `lookahead_on` contract
- manual lower-TF fail-closed guard

## TradingView acceptance

Recommended:
- XAGUSD 1H
- BTCUSDT 1H
- SOLUSDT 4H

Steps:
1. Compile with zero errors.
2. Check 1H → 2H → 4H → 1D in Auto mode.
3. Confirm dashboard TF stack changes automatically.
4. Confirm %K / %D render.
5. Enable individual signals and confirm event markers.
6. Verify MTF consensus labels.
7. Reload and compare historical output.
8. Configure one static alert and one `alert()` JSON alert.
