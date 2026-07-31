import os


def ft_tqdm(lst: range) -> None:
    """Simulate a progress bar for a given
     list of items, displaying the percentage
     of completion and the number of items processed."""
    total = len(lst)
    bar_length = os.get_terminal_size().columns - 41
    for i, elem in enumerate(lst):
        progress = (i + 1) / total
        percent = int(progress * 100)
        filled = int(bar_length * progress)
        bar = "-" * filled + " " * (bar_length - filled)
        print(f"\r{percent:>3}%|{bar}>| {i+1}/{total}", end="", flush=True)
        os.system("sleep 0.01")
        yield elem
