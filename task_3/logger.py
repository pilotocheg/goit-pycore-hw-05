from constants import LEVELS
from helpers import filter_logs_by_level


def display_log_counts(counts: dict):
    info = f"""
Рівень логування | Кількість
-----------------|----------
{LEVELS.info}             | {counts[LEVELS.info]}
{LEVELS.debug}            | {counts[LEVELS.debug]}
{LEVELS.error}            | {counts[LEVELS.error]}
{LEVELS.warning}          | {counts[LEVELS.warning]}
"""
    print(info)


def display_logs_for_level(logs: list[dict], level: str):
    uppercase_level = level.upper()

    if not uppercase_level in LEVELS:
        print(
            f"Рівень '{level}' не підтримується. Виберіть один із варіантів:",
            ",".join(LEVELS),
        )
        return

    level_logs = filter_logs_by_level(logs, uppercase_level)

    if not len(level_logs):
        print(f"Не знайдено логів для рівня '{level}'.")
        return

    print(f"Деталі логів для рівня '{level}':")

    for log in level_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")
