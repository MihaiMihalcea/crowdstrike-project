# main.py
import os
from datetime import datetime
import argparse
from data_generator import save_opportunities_to_csv
from scorer import Scorer

def make_run_folder(root="runs"):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.join(root, ts)
    os.makedirs(path, exist_ok=True)
    return path

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
    args = parse_args()
    run_folder = make_run_folder()
    synth_path = os.path.join(run_folder, "synthetic_opportunities.csv")
    scored_path = os.path.join(run_folder, "scored_opportunities.csv")

    if not args.skip_generate:
        print("🔹 Generating synthetic opportunities…")
        save_opportunities_to_csv(filename=synth_path)  # defaults to 50 rows and synthetic_opportunities.csv
    else:
        print("⚠️  Skipping data generation")

    if not args.skip_score:
        print("🔹 Scoring opportunities via OpenAI…")
        Scorer(input_file=synth_path, output_file=scored_path).run()  # reads synthetic_opportunities.csv & writes scored_opportunities.csv
    else:
        print("⚠️  Skipping scoring step")

    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
