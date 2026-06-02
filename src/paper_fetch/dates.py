from datetime import datetime, timedelta

def parse_since(since: str) -> datetime:
    if not since.endswith("d"):
        raise ValueError(
            "Invalid format. Use values like 7d, 30d, 90d."
        )

    try:
        days = int(since[:-1])
    except ValueError:
        raise ValueError(
            "Days must be a number."
        )

    return datetime.now() - timedelta(days=days)