from collections import defaultdict


def filter_logs_by_level(logs: list, level: str) -> list[dict]:
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict[str, int]:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1

    return counts
