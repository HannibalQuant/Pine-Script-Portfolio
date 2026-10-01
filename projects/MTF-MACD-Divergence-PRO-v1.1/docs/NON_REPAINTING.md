# Non-Repainting Contract

The indicator treats non-repainting behavior as a design constraint, not a label.

## Higher-timeframe requests

Requested values are shifted inside the requested context:

```pine
[rb[1], rbe[1], hb[1], hbe[1], m[1], s[1], h[1], time[1]]
```

and consumed through:

```pine
lookahead = barmerge.lookahead_on
```

The important detail is that `lookahead_on` is not used with a developing requested-timeframe value. The payload is already offset to the previous fully closed requested bar.

## Pivot confirmation

`ta.pivotlow()` / `ta.pivothigh()` require right-side bars before a pivot becomes known. Therefore divergence signals are intentionally delayed by the configured `rightBars` confirmation period.

## Auto vs Manual timeframe mode

Auto mode only resolves same-or-higher timeframe contexts. Manual mode fails closed when the user selects a lower-than-chart timeframe because lower-timeframe aggregation requires different semantics.

## Alert timing

Dynamic JSON alerts require `barstate.isconfirmed` and use `alert.freq_once_per_bar_close`.

## Verification boundary

TradingView runtime compatibility and adaptive timeframe switching have been verified. Formal realtime observation across a higher-timeframe close and end-to-end alert delivery remain separate checks.
