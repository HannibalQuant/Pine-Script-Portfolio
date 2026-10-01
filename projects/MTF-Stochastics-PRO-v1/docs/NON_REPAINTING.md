# Non-Repainting Contract

The project uses confirmed requested-timeframe values.

`f_confirmedPack()` offsets every requested value by `[1]`, and the security calls use `barmerge.lookahead_on`.

This means a developing higher-timeframe bar is not treated as final historical information.

## Auto mode

Auto mode selects the chart timeframe plus standard same-or-higher timeframes.

## Manual mode

Manual mode rejects lower-than-chart requests. Lower-timeframe aggregation has different semantics and should be implemented explicitly rather than hidden behind a normal HTF request.

## Alert timing

Dynamic JSON alerts require `barstate.isconfirmed` and use `alert.freq_once_per_bar_close`.

## Remaining runtime checks

Before calling the project fully runtime-verified:
- compile it in TradingView
- switch across several chart intervals
- reload the chart and compare historical signals
- observe behavior across an HTF close
- verify alert delivery
