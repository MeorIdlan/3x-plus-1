import matplotlib.pyplot as plt
from pathlib import Path

def collatz_sequence(n: int):
    """Return the Collatz sequence starting at n, ending at 1 (inclusive)."""
    if n < 1:
        raise ValueError("Seed must be a positive integer.")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def plot_collatz(seed: int, log_y: bool = False,
                 save_png: bool = False, out_dir: str = "graphs",
                 filename: str | None = None, dpi: int = 150):
    seq = collatz_sequence(seed)
    x = list(range(len(seq)))

    fig = plt.figure()
    plt.plot(x, seq, marker='o')  # simple line + points
    plt.title(f"Collatz trajectory from {seed}  |  steps={len(seq)-1}, max={max(seq)}")
    plt.xlabel("Step")
    plt.ylabel("Value (n)")
    if log_y:
        plt.yscale("log")
        plt.ylabel("Value (log scale)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    if save_png:
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        if not filename:
            filename = f"collatz_{seed}_steps{len(seq)-1}_max{max(seq)}.png"
        if not filename.lower().endswith(".png"):
            filename += ".png"
        out_path = Path(out_dir) / filename
        fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
        print(f"Saved figure to {out_path.resolve()}")

    plt.show()