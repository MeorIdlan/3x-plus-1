import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Plot a Collatz (3x+1) trajectory and optionally save a PNG."
    )
    p.add_argument("-s", "--seed", type=int, help="Positive integer starting seed.")
    p.add_argument("--log", dest="log_y", action="store_true", help="Use log-scale y-axis.")
    p.add_argument("--no-log", dest="log_y", action="store_false", help="Do not use log-scale y-axis.")
    p.set_defaults(log_y=None)  # None => ask interactively

    p.add_argument("--save", dest="save_png", action="store_true", help="Save PNG to ./graphs (or --out-dir).")
    p.add_argument("--no-save", dest="save_png", action="store_false", help="Do not save PNG.")
    p.set_defaults(save_png=None)  # None => ask interactively

    p.add_argument("-o", "--out-dir", default=None, help="Output directory (default: graphs).")
    p.add_argument("-f", "--filename", default=None, help="Output filename ('.png' appended if missing).")
    p.add_argument("--dpi", type=int, default=None, help="PNG DPI (default: 150).")
    return p