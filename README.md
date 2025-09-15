# Collatz Trajectory Plotter (Matplotlib)

Plot the Collatz (3x+1) trajectory for any positive integer seed. Pass options via CLI **or** skip them and you’ll be prompted interactively. You can also save the plot as a PNG to `./graphs`.

## Features

* Generates the full Collatz sequence from a given seed (ending at 1, inclusive)
* Clean Matplotlib line plot with optional log-scale y-axis
* Optional PNG export (auto-named or custom filename) to `./graphs`
* Dual UX:

  * **CLI flags** for scripting/automation
  * **Interactive prompts** when flags are omitted

## Requirements

* Python 3.8+
* `matplotlib`

## Installation

```bash
# clone your repo, then:
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # or: pip install matplotlib
```

`requirements.txt` (minimal)

```
matplotlib>=3.5
```

## Usage

### 1) Fully interactive (no flags)

```bash
python main.py
```

You’ll be asked for:

* seed (positive integer)
* whether to use a log-scale y-axis
* whether to save a PNG (and optionally filename/DPI)

### 2) CLI flags (no prompts)

```bash
python main.py --seed 27 --save --log --dpi 200 -o graphs -f my_27_plot.png
```

### 3) Mixed (some flags, prompt for the rest)

```bash
python main.py --seed 97 --save
# You’ll be prompted for anything you didn’t specify (e.g., log-scale, filename/DPI).
```

### Command reference

```
usage: main.py [-h] [-s SEED] [--log | --no-log]
                       [--save | --no-save] [-o OUT_DIR]
                       [-f FILENAME] [--dpi DPI]

options:
  -h, --help            show this help message and exit
  -s, --seed            Positive integer starting seed
  --log                 Use log-scale y-axis
  --no-log              Do not use log-scale y-axis
  --save                Save PNG to ./graphs (or --out-dir)
  --no-save             Do not save PNG
  -o, --out-dir         Output directory (default: graphs)
  -f, --filename        Output filename ('.png' appended if missing)
  --dpi                 PNG DPI (default: 150)
```

## What gets generated?

* **On-screen plot** of the trajectory (step vs. value)
* **Optional PNG** at `./graphs/<filename>`.
  If you don’t specify `--filename`, an auto name is used, e.g.:

  ```
  collatz_27_steps111_max9232.png
  ```

## Example

```bash
python main.py --seed 27 --log --save
# Saved figure to /full/path/graphs/collatz_27_steps111_max9232.png
```

## Tips & troubleshooting

* **Headless servers/CI**: Matplotlib may need a non-GUI backend.

  * Option A: Set an environment variable:

    ```bash
    MPLBACKEND=Agg python main.py --seed 100 --save --no-log
    ```
  * Option B: Run in an environment with an available display (e.g., local machine).
* **Permission errors when saving**: Ensure you have write access to the repo directory or change `--out-dir`.
* **“Seed must be a positive integer.”**: Provide `--seed` ≥ 1.

## Contributing

Issues and PRs are welcome: tidy code, clear messages, and small, focused changes please.

## License

MIT License — see `LICENSE` for details.
