# main.py
import argparse
from data_generator import save_opportunities_to_csv
from scorer import Scorer

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

    if not args.skip_generate:
        print("🔹 Generating synthetic opportunities…")
        save_opportunities_to_csv()  # defaults to 50 rows and synthetic_opportunities.csv
    else:
        print("⚠️  Skipping data generation")

    if not args.skip_score:
        print("🔹 Scoring opportunities via OpenAI…")
        Scorer().run()  # reads synthetic_opportunities.csv & writes scored_opportunities.csv
    else:
        print("⚠️  Skipping scoring step")

    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
