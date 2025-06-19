# main.py
import os
import argparse
from datetime import datetime
from data_generator import save_opportunities_to_csv
from scorer import Scorer

RUN_ROOT = "runs"

def make_run_folder(root="runs"):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(root, ts)
    os.makedirs(path, exist_ok=True)
    return path

def find_latest_run_folder(root=RUN_ROOT):
    """
    Find the most recent timestamped folder under `root`.
    Raises if none exist.
    """
    if not os.path.isdir(root):
        raise FileNotFoundError(f"No runs directory found at {root}")
    # list only directories that look like timestamps
    candidates = [
        d for d in os.listdir(root)
        if os.path.isdir(os.path.join(root, d))
    ]
    if not candidates:
        raise FileNotFoundError(f"No subfolders in runs/ to score from")
    # sort lexicographically—ISO timestamps sort correctly
    latest = sorted(candidates)[-1]
    return os.path.join(root, latest)

def parse_args():
    p = argparse.ArgumentParser(
        description="1) Generate synthetic opportunities, 2) Score them via OpenAI"
    )
    p.add_argument(
        "--skip-generate", action="store_true",
        help="Don't generate new synthetic data; use existing CSV"
    )
    p.add_argument(
        "--skip-score", action="store_true",
        help="Don't run scoring; only generate data"
    )
    return p.parse_args()

def main():
    """
    CLI entry point. Orchestrates:
      1) data generation via data_generator
      2) scoring via Scorer
    """
    args = parse_args()
    # Decide run_folder based on skip_generate
    if args.skip_generate:
        run_folder = find_latest_run_folder()
        print(f"ℹ️  Skipping generation, using folder: {run_folder}")
    else:
        run_folder = make_run_folder()
        print(f"🔹 Generating synthetic opportunities into: {run_folder}")
        save_opportunities_to_csv(
            filename=os.path.join(run_folder, "synthetic_opportunities.csv")
        )

    if not args.skip_score:
        synth_path = os.path.join(run_folder, "synthetic_opportunities.csv")
        scored_path = os.path.join(run_folder, "scored_opportunities.csv")
        print(f"🔹 Scoring opportunities from {synth_path} → {scored_path}")
        Scorer(input_file=synth_path, output_file=scored_path).run()
    else:
        print("⚠️  Skipping scoring step")

    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
