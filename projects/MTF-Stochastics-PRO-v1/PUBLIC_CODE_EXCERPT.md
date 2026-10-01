# Public Code Excerpt — MTF Stochastics PRO v1

This file is intentionally **not a complete indicator**. It shows the public engineering pattern only; proprietary signal classification, MTF consensus state, and alert logic are omitted.

```pine
//@version=6
indicator("MTF Stochastics PRO v1 — excerpt", overlay = false)

int kLength = input.int(14, "%K length", minval = 1)
int dLength = input.int(3, "%D smoothing", minval = 1)
string tfMode = input.string("Auto", "Timeframe mode", options = ["Auto", "Manual"])

string tf1 = tfMode == "Auto" ? timeframe.period : input.timeframe("60", "TF1")
string tf2 = "<private resolver>"
string tf3 = "<private resolver>"

// Proprietary oscillator/signal engine omitted.
// f_privateConfirmedPack(...) returns only previously closed requested-TF data.

[bullEvent1, bearEvent1, k1, d1] = request.security(
    syminfo.tickerid,
    tf1,
    f_privateConfirmedPack(...),
    gaps = barmerge.gaps_off,
    lookahead = barmerge.lookahead_on)

// Private implementation continues with:
// - reversal and momentum signal families
// - MTF confirmation window
// - dashboard state
// - static + JSON alerts
```

The complete compile-ready source remains private.
