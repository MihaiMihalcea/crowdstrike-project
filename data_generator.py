import pandas as pd
from main import generate_opportunity  # Adjust path if needed

def generate_opportunity_dataframe(num_opportunities=50):
    opportunities = [generate_opportunity(i) for i in range(num_opportunities)]
    df = pd.DataFrame(opportunities)
    return df

def save_opportunities_to_csv(filename="synthetic_opportunities.csv", num_opportunities=50):
    df = generate_opportunity_dataframe(num_opportunities)
    df.to_csv(filename, index=False)
    print(f"CSV file saved as '{filename}'")

# Optional: run when script is executed directly
if __name__ == "__main__":
    save_opportunities_to_csv()
