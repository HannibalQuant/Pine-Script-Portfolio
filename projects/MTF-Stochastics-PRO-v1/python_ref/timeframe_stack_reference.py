"""Reference model for the adaptive timeframe ladder."""

STANDARD = [
    ("60", 60 * 60),
    ("240", 4 * 60 * 60),
    ("1D", 24 * 60 * 60),
    ("1W", 7 * 24 * 60 * 60),
    ("1M", 30 * 24 * 60 * 60),
    ("3M", 90 * 24 * 60 * 60),
    ("6M", 180 * 24 * 60 * 60),
    ("12M", 360 * 24 * 60 * 60),
]


def auto_stack(chart_label: str, chart_seconds: int) -> tuple[str, str, str]:
    higher = [label for label, seconds in STANDARD if seconds > chart_seconds]
    tf2 = higher[0] if len(higher) >= 1 else chart_label
    tf3 = higher[1] if len(higher) >= 2 else chart_label
    return chart_label, tf2, tf3
