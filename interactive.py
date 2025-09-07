def ask_yes_no(question: str, default: bool | None = None) -> bool:
    """Prompt user for yes/no. Returns True/False. Default used on empty input."""
    if default is True:
        suffix = " [Y/n]: "
    elif default is False:
        suffix = " [y/N]: "
    else:
        suffix = " [y/n]: "
    while True:
        ans = input(question + suffix).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        if ans == "" and default is not None:
            return default
        print("Please enter 'y' or 'n'.")

def ask_positive_int(prompt: str, default: int | None = None) -> int:
    """Prompt for a positive integer."""
    while True:
        raw = input(f"{prompt}" + (f" (default {default}): " if default is not None else ": ")).strip()
        if raw == "" and default is not None:
            return default
        try:
            val = int(raw)
            if val > 0:
                return val
        except ValueError:
            pass
        print("Please enter a positive integer.")

def ask_optional_str(prompt: str) -> str | None:
    """Prompt for an optional string; returns None if blank."""
    s = input(f"{prompt} (leave blank for automatic): ").strip()
    return s if s else None