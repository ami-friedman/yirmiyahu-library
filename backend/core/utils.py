from datetime import datetime


def human_readable_ts(ts: int) -> str:
    return datetime.fromtimestamp(ts).strftime('%b %d %Y')

