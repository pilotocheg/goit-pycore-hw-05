import sys


def get_sys_arg(index: int) -> str | None:
    try:
        return sys.argv[index]
    except:
        return None
