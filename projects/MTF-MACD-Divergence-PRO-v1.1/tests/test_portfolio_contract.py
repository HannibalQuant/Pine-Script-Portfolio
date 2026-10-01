from pathlib import Path
import re
import numpy as np
import pytest

from python_ref.divergence_reference import detect_divergences
from python_ref.timeframe_stack_reference import auto_stack

PINE = Path("pine/MTF_MACD_Divergence_PRO_v1_1.pine").read_text(encoding="utf-8")
CODE = "\n".join(line.split("//", 1)[0] for line in PINE.splitlines())


def _base(n=30):
    low = np.full(n, 100.0)
    high = np.full(n, 110.0)
    osc = np.zeros(n)
    return low, high, osc


def test_regular_bullish_confirmation_delay():
    low, high, osc = _base()
    osc[:] = 4.0
    osc[4:9] = [3, 2, -3, 2, 3]
    osc[14:19] = [3, 2, -1, 2, 3]
    low[6] = 95.0
    low[16] = 90.0

    events = detect_divergences(low, high, osc, left=2, right=2, min_span=5, max_span=20)
    bulls = [e for e in events if e.kind == "regular_bullish"]

    assert len(bulls) == 1
    assert bulls[0].pivot_index == 16
    assert bulls[0].confirm_index == 18


def test_hidden_bearish_detection():
    low, high, osc = _base()
    osc[:] = -4.0
    osc[4:9] = [-3, -2, 1, -2, -3]
    osc[14:19] = [-3, -2, 3, -2, -3]
    high[6] = 120.0
    high[16] = 115.0

    events = detect_divergences(low, high, osc, left=2, right=2, min_span=5, max_span=20)
    assert "hidden_bearish" in [e.kind for e in events]


def test_reference_fails_closed_on_length_mismatch():
    with pytest.raises(ValueError):
        detect_divergences([1, 2], [2], [0, 1], left=1, right=1)


def test_auto_timeframe_stack():
    assert auto_stack("15", 15 * 60) == ("15", "60", "240")
    assert auto_stack("60", 60 * 60) == ("60", "240", "1D")
    assert auto_stack("240", 4 * 60 * 60) == ("240", "1D", "1W")
    assert auto_stack("1D", 24 * 60 * 60) == ("1D", "1W", "1M")


def test_pine_v6_and_version_contract():
    assert PINE.lstrip().startswith("//@version=6")
    assert 'MTF MACD Divergence PRO v1.1' in CODE
    assert 'shorttitle = "MTFMDIV11"' in CODE


def test_confirmed_mtf_request_contract():
    assert CODE.count("request.security(") == 3
    assert CODE.count("lookahead = barmerge.lookahead_on") == 3
    assert "[rb[1], rbe[1], hb[1], hbe[1], m[1], s[1], h[1], time[1]]" in CODE


def test_auto_mode_default_and_manual_guard():
    assert 'input.string("Auto", "Timeframe mode"' in CODE
    assert 'string tf1 = autoMode ? timeframe.period : manualTf1' in CODE
    assert CODE.count("must be equal to or higher than the chart timeframe") == 3


def test_no_bare_assignment_at_end_of_code_line():
    offenders = [line.rstrip() for line in CODE.splitlines() if line.strip() and line.rstrip().endswith("=")]
    assert offenders == []


def test_shorttitle_limit():
    match = re.search(r'shorttitle\s*=\s*"([^"]+)"', CODE)
    assert match is not None
    assert len(match.group(1)) <= 10
