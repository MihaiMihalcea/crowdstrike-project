import random
import csv
import pandas as pd
from opportunity_generator import generate_opportunity  # updated below to accept a flag

def generate_opportunity_dataframe(num_opportunities: int = 50) -> pd.DataFrame:
    # 1. Build a list with exactly half True (include MEDDPICC) and half False
    half = num_opportunities // 2
    flags = [True]*half + [False]*(num_opportunities - half)
    random.shuffle(flags)

    # 2. Generate each opportunity with the corresponding flag
    opportunities = [
        generate_opportunity(i, include_meddpicc=flags[i])
        for i in range(num_opportunities)
    ]
    return pd.DataFrame(opportunities)

def save_opportunities_to_csv(
    filename: str,
    num_opportunities: int = 50
) -> None:
    """
    Generate synthetic opportunities and save to CSV.

    Args:
        filename (str): Path to output CSV file.
        num_opportunities (int): Number of opportunities to generate.

    Returns:
        None
    """
    df = generate_opportunity_dataframe(num_opportunities)
    df.to_csv(
        filename,
        index=False,
        header=True,
        encoding="utf-8-sig",
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n"
    )
    print(f"CSV file saved as '{filename}'")

