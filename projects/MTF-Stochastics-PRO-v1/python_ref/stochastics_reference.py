"""Python reference logic for MTF Stochastics PRO v1."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class StochSignals:
    bull_reversal: pd.Series
    bear_reversal: pd.Series
    bull_momentum: pd.Series
    bear_momentum: pd.Series
    k: pd.Series
    d: pd.Series


def stochastic(
    high: Iterable[float],
    low: Iterable[float],
    close: Iterable[float],
    k_length: int = 14,
    smooth_k: int = 3,
    d_length: int = 3,
) -> tuple[pd.Series, pd.Series]:
    h = pd.Series(high, dtype="float64")
    l = pd.Series(low, dtype="float64")
    c = pd.Series(close, dtype="float64")
    if not (len(h) == len(l) == len(c)):
        raise ValueError("high, low and close must have equal lengths")
    if min(k_length, smooth_k, d_length) < 1:
        raise ValueError("all stochastic lengths must be >= 1")

    hh = h.rolling(k_length, min_periods=k_length).max()
    ll = l.rolling(k_length, min_periods=k_length).min()
    span = hh - ll

    raw_k = 100.0 * (c - ll) / span.replace(0.0, np.nan)
    k = raw_k.rolling(smooth_k, min_periods=smooth_k).mean()
    d = k.rolling(d_length, min_periods=d_length).mean()
    return k, d


def signal_engine(
    k: Iterable[float],
    d: Iterable[float],
    overbought: float = 80.0,
    oversold: float = 20.0,
    midline: float = 50.0,
    require_alignment: bool = True,
) -> StochSignals:
    ks = pd.Series(k, dtype="float64")
    ds = pd.Series(d, dtype="float64")
    if len(ks) != len(ds):
        raise ValueError("k and d must have equal lengths")
    if oversold >= overbought:
        raise ValueError("oversold must be below overbought")

    cross_up = (ks > ds) & (ks.shift(1) <= ds.shift(1))
    cross_down = (ks < ds) & (ks.shift(1) >= ds.shift(1))

    bull_reversal = cross_up & pd.concat([ks, ds], axis=1).min(axis=1).le(oversold)
    bear_reversal = cross_down & pd.concat([ks, ds], axis=1).max(axis=1).ge(overbought)

    mid_up = (ks > midline) & (ks.shift(1) <= midline)
    mid_down = (ks < midline) & (ks.shift(1) >= midline)

    bull_momentum = mid_up & ((ks > ds) if require_alignment else True)
    bear_momentum = mid_down & ((ks < ds) if require_alignment else True)

    return StochSignals(
        bull_reversal=bull_reversal.fillna(False),
        bear_reversal=bear_reversal.fillna(False),
        bull_momentum=pd.Series(bull_momentum, index=ks.index).fillna(False),
        bear_momentum=pd.Series(bear_momentum, index=ks.index).fillna(False),
        k=ks,
        d=ds,
    )
