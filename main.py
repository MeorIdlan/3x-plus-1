import sys
from collatz import plot_collatz
from interactive import ask_positive_int, ask_yes_no
from cli import build_parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    # Seed (required overall, but optional via CLI => prompt if missing)
    if args.seed is None:
        try:
            seed = ask_positive_int("Enter a positive integer seed")
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.", file=sys.stderr)
            sys.exit(1)
    else:
        seed = args.seed
        if seed < 1:
            print("Error: seed must be a positive integer.", file=sys.stderr)
            sys.exit(1)

    # Log-scale?
    log_y = args.log_y if args.log_y is not None else ask_yes_no("Use log-scale y-axis?", default=False)

    # Save?
    save_png = args.save_png if args.save_png is not None else ask_yes_no("Save PNG to ./graphs?", default=False)

    # If saving, fill optional details (prompt only for those not provided)
    out_dir = args.out_dir or ("graphs" if save_png else None)
    filename = args.filename
    dpi = args.dpi if args.dpi is not None else (ask_positive_int("DPI for saved PNG", default=150) if save_png else 150)

    try:
        plot_collatz(
            seed=seed,
            log_y=log_y,
            save_png=save_png,
            out_dir=out_dir or "graphs",
            filename=filename if save_png else None,
            dpi=dpi,
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()