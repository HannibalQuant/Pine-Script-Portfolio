"""Reference divergence engine for portfolio validation.

This is not a TradingView replacement. It mirrors the pivot-comparison rules
used by the Pine indicator so the classification logic can be unit-tested.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class DivergenceEvent:
    confirm_index: int
    pivot_index: int
    previous_pivot_index: int
    kind: str


def macd(close: Iterable[float], fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    s = pd.Series(close, dtype="float64")
    fast_ema = s.ewm(span=fast, adjust=False).mean()
    slow_ema = s.ewm(span=slow, adjust=False).mean()
    line = fast_ema - slow_ema
    sig = line.ewm(span=signal, adjust=False).mean()
    return pd.DataFrame({"macd": line, "signal": sig, "hist": line - sig})


def _is_pivot_low(x: np.ndarray, i: int, left: int, right: int) -> bool:
    if i - left < 0 or i + right >= len(x):
        return False
    center = x[i]
    window = x[i-left:i+right+1]
    return np.isfinite(center) and center == np.nanmin(window) and np.sum(window == center) == 1


def _is_pivot_high(x: np.ndarray, i: int, left: int, right: int) -> bool:
    if i - left < 0 or i + right >= len(x):
        return False
    center = x[i]
    window = x[i-left:i+right+1]
    return np.isfinite(center) and center == np.nanmax(window) and np.sum(window == center) == 1


def detect_divergences(
    low: Iterable[float],
    high: Iterable[float],
    oscillator: Iterable[float],
    left: int = 5,
    right: int = 5,
    min_span: int = 5,
    max_span: int = 80,
) -> List[DivergenceEvent]:
    """Detect regular/hidden divergence using confirmed oscillator pivots.

    A pivot at index i is confirmed at i + right, matching ta.pivot* semantics.
    """
    lows = np.asarray(list(low), dtype=float)
    highs = np.asarray(list(high), dtype=float)
    osc = np.asarray(list(oscillator), dtype=float)

    if not (len(lows) == len(highs) == len(osc)):
        raise ValueError("low, high and oscillator must have equal lengths")

    events: List[DivergenceEvent] = []
    previous_low_pivot = None
    previous_high_pivot = None

    for i in range(len(osc)):
        if _is_pivot_low(osc, i, left, right):
            if previous_low_pivot is not None:
                span = i - previous_low_pivot
                if min_span <= span <= max_span:
                    if lows[i] < lows[previous_low_pivot] and osc[i] > osc[previous_low_pivot]:
                        events.append(DivergenceEvent(i + right, i, previous_low_pivot, "regular_bullish"))
                    if lows[i] > lows[previous_low_pivot] and osc[i] < osc[previous_low_pivot]:
                        events.append(DivergenceEvent(i + right, i, previous_low_pivot, "hidden_bullish"))
            previous_low_pivot = i

        if _is_pivot_high(osc, i, left, right):
            if previous_high_pivot is not None:
                span = i - previous_high_pivot
                if min_span <= span <= max_span:
                    if highs[i] > highs[previous_high_pivot] and osc[i] < osc[previous_high_pivot]:
                        events.append(DivergenceEvent(i + right, i, previous_high_pivot, "regular_bearish"))
                    if highs[i] < highs[previous_high_pivot] and osc[i] > osc[previous_high_pivot]:
                        events.append(DivergenceEvent(i + right, i, previous_high_pivot, "hidden_bearish"))
            previous_high_pivot = i

    return events
