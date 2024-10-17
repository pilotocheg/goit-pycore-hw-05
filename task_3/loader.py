import re
from constants import LEVELS


def parse_log_line(line: str) -> dict[str, str] | None:
    m = re.match(
        r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>"
        + "|".join(LEVELS)
        + r") (?P<message>.+)",
        line,
    )

    return m and m.groupdict()


def load_logs(file_path: str) -> list[dict[str, str]]:
    logs = []

    with open(file_path, "r", encoding="utf8") as file:
        for line in file:
            log = parse_log_line(line)
            if log:
                logs.append(log)

    return logs
