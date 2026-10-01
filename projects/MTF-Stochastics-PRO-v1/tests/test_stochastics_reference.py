import numpy as np
import pytest

from python_ref.stochastics_reference import signal_engine, stochastic


def test_stochastic_range_and_shapes():
    high = np.arange(1.0, 41.0) + 2.0
    low = np.arange(1.0, 41.0) - 2.0
    close = np.arange(1.0, 41.0)
    k, d = stochastic(high, low, close, k_length=5, smooth_k=3, d_length=3)

    assert len(k) == 40
    assert len(d) == 40
    assert k.dropna().between(0, 100).all()
    assert d.dropna().between(0, 100).all()


def test_bullish_reversal_in_oversold_zone():
    k = [25, 18, 17, 19]
    d = [24, 20, 18, 18]
    s = signal_engine(k, d, overbought=80, oversold=20)
    assert bool(s.bull_reversal.iloc[3])


def test_bearish_reversal_in_overbought_zone():
    k = [75, 84, 83, 81]
    d = [76, 82, 82, 82]
    s = signal_engine(k, d, overbought=80, oversold=20)
    assert bool(s.bear_reversal.iloc[3])


def test_bullish_midline_momentum_with_alignment():
    k = [45, 49, 52]
    d = [44, 48, 50]
    s = signal_engine(k, d, midline=50, require_alignment=True)
    assert bool(s.bull_momentum.iloc[2])


def test_bearish_midline_momentum_with_alignment():
    k = [55, 51, 48]
    d = [56, 52, 50]
    s = signal_engine(k, d, midline=50, require_alignment=True)
    assert bool(s.bear_momentum.iloc[2])


def test_alignment_filter_blocks_wrong_side():
    k = [45, 49, 52]
    d = [44, 48, 55]
    s = signal_engine(k, d, midline=50, require_alignment=True)
    assert not bool(s.bull_momentum.iloc[2])


def test_invalid_thresholds_fail_closed():
    with pytest.raises(ValueError):
        signal_engine([1, 2], [1, 2], overbought=20, oversold=80)


def test_length_mismatch_fails_closed():
    with pytest.raises(ValueError):
        stochastic([1, 2], [0], [1, 2], k_length=1, smooth_k=1, d_length=1)
