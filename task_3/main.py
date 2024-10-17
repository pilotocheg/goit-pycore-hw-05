from utils import get_sys_arg
from helpers import count_logs_by_level
from logger import display_log_counts, display_logs_for_level
from loader import load_logs


def main():
    file_path = get_sys_arg(1)

    if not file_path:
        print("Provide file path as the first argument")
        return

    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        level = get_sys_arg(2)
        if level:
            display_logs_for_level(logs, level)

    except FileNotFoundError:
        print(f"File not found by path '{file_path}'")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
