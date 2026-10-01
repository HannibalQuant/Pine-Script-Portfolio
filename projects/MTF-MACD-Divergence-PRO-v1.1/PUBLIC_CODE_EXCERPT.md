# Public Code Excerpt — MTF MACD Divergence PRO v1.1

This file is intentionally **not a complete indicator**. It shows the public engineering pattern only; proprietary divergence detection, signal classification, state handling, and alert payload logic are omitted.

```pine
//@version=6
indicator("MTF MACD Divergence PRO v1.1 — excerpt", overlay = false)

string tfMode = input.string("Auto", "Timeframe mode", options = ["Auto", "Manual"])
string tf1 = tfMode == "Auto" ? timeframe.period : input.timeframe("60", "TF1")

// The private implementation resolves higher TFs and validates manual inputs.
string tf2 = "<private resolver>"
string tf3 = "<private resolver>"

// Proprietary divergence engine omitted.
// f_privateConfirmedPack(...) returns only previously closed requested-TF data.

[signal1, macd1, signalLine1] = request.security(
    syminfo.tickerid,
    tf1,
    f_privateConfirmedPack(...),
    gaps = barmerge.gaps_off,
    lookahead = barmerge.lookahead_on)

// Private implementation continues with:
// - pivot-confirmed divergence classification
// - regular / hidden bullish and bearish logic
// - MTF confirmation window
// - dashboard state
// - static + JSON alerts
```

The complete compile-ready source remains private.
