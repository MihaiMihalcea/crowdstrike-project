import pandas as pd

opportunities = [generate_opportunity(i) for i in range(50)]
df = pd.DataFrame(opportunities)

df.to_csv("synthetic_opportunities.csv", index=False)
print("CSV file saved!")
