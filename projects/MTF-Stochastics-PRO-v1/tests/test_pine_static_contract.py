from pathlib import Path
import re

PINE = Path("pine/MTF_Stochastics_PRO_v1.pine").read_text(encoding="utf-8")


def _without_comments(source: str) -> str:
    return "\n".join(line.split("//", 1)[0] for line in source.splitlines())


CODE = _without_comments(PINE)


def test_pine_v6_declared():
    assert PINE.lstrip().startswith("//@version=6")


def test_shorttitle_limit():
    m = re.search(r'shorttitle\s*=\s*"([^"]+)"', CODE)
    assert m is not None
    assert len(m.group(1)) <= 10


def test_exactly_three_security_calls():
    assert CODE.count("request.security(") == 3
    assert CODE.count("lookahead = barmerge.lookahead_on") == 3


def test_confirmed_pack_offsets_payload():
    expected = "[br[1], sr[1], bm[1], sm[1], k[1], d[1], time[1]]"
    assert expected in CODE


def test_auto_mode_is_default():
    assert 'input.string("Auto", "Timeframe mode"' in CODE
    assert 'string tf1 = autoMode ? timeframe.period : manualTf1' in CODE
    assert "f_autoTf2(chartTfSec)" in CODE
    assert "f_autoTf3(chartTfSec)" in CODE


def test_manual_lower_tf_fail_closed():
    assert CODE.count("must be equal to or higher than the chart timeframe") == 3


def test_signal_families_present():
    assert "bullReversal" in CODE
    assert "bearReversal" in CODE
    assert "bullMomentum" in CODE
    assert "bearMomentum" in CODE


def test_no_bare_assignment_line():
    offenders = [line for line in CODE.splitlines() if line.rstrip().endswith("=")]
    assert offenders == []
