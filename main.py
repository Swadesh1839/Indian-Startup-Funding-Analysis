# Step 1: Import libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  Step 2: Load dataset 
df = pd.read_csv("/content/startup_funding.csv")

# Step 3: Inspect data
print(df.head())
print(df.info())

#  Step 4: Clean & preprocess 
# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where date is missing
df = df.dropna(subset=['date'])

# Fill or drop other null values
df['industry_vertical'] = df['industry_vertical'].fillna('Unknown')
df['city/location'] = df['city/location'].fillna('Unknown')
df['investors_name'] = df['investors_name'].fillna('Undisclosed')

# Remove commas, convert to numeric for amount
df['amount_in_usd'] = df['amount_in_usd'].replace('[\$,]', '', regex=True)
df['amount_in_usd'] = pd.to_numeric(df['amount_in_usd'], errors='coerce')

# Step 5: Funding trends over time 
funding_trend = df.groupby(df['date'].dt.to_period('M'))['amount_in_usd'].sum()
funding_trend.plot(kind='line', figsize=(12,6), marker='o')
plt.title("Funding Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Funding (USD)")
plt.show()

#  Step 6: Top sectors 
top_sectors = df['industry_vertical'].value_counts().head(10)
sns.barplot(x=top_sectors.values, y=top_sectors.index)
plt.title("Top 10 Sectors by Number of Fundings")
plt.xlabel("Number of Fundings")
plt.show()

#  Step 7: Top cities 
top_cities = df['city/location'].value_counts().head(10)
sns.barplot(x=top_cities.values, y=top_cities.index)
plt.title("Top 10 Cities by Number of Fundings")
plt.xlabel("Number of Fundings")
plt.show()

# Step 8: Top startups 
top_startups = df['startup_name'].value_counts().head(10)
sns.barplot(x=top_startups.values, y=top_startups.index)
plt.title("Top 10 Startups by Funding Count")
plt.xlabel("Number of Fundings")
plt.show()

#  Step 9: Active investors
active_investors = df['investors_name'].value_counts().head(10)
sns.barplot(x=active_investors.values, y=active_investors.index)
plt.title("Top 10 Active Investors")
plt.xlabel("Number of Investments")
plt.show()

# Step 10: Investment type distribution (Top 10 only)
# Clean and standardize investment_type
df['investmentntype'] = df['investmentntype'].str.strip().str.title()
df['investmentntype'] = df['investmentntype'].replace({
    'Seed/ Angel Funding': 'Seed Funding',
    'Seed / Angel Funding': 'Seed Funding',
    'Seed\\Nfunding': 'Seed Funding',
    'Seed/Angel Funding': 'Seed Funding',
    'Angel / Seed Funding': 'Seed Funding',
    'Seed Round': 'Seed Funding',
    'Seed': 'Seed Funding',
    'Seed Funding Round': 'Seed Funding',
    'Angel Round': 'Seed Funding',
    'Angel': 'Seed Funding',
    'Private Equity Round': 'Private Equity',
    'Private\\Nequity': 'Private Equity',
    'Private Funding': 'Private Equity',
    'Private': 'Private Equity',
    'Debt-Funding': 'Debt Funding',
    'Debt And Preference Capital': 'Debt Funding',
    'Pre-Series A': 'Pre Series A',
    'Pre Series A': 'Pre Series A',
    'Series A': 'Series A',
    'Series B': 'Series B',
    'Series C': 'Series C',
    'Series D': 'Series D',
    'Series E': 'Series E',
    'Series J': 'Series J'
})


# Count and sort investment types, keep top 10
investment_counts = df['investmentntype'].value_counts().reset_index().head(10)
investment_counts.columns = ['Investment Type', 'Count']

# Plot top 10
plt.figure(figsize=(8, 5))
sns.barplot(
    x='Count',
    y='Investment Type',
    data=investment_counts,
    palette='viridis'
)
plt.title("Top 10 Investment Types", fontsize=14)
plt.xlabel("Number of Investments")
plt.ylabel("Investment Type")
plt.tight_layout()
plt.show()
#Step 11: Recommendations
print("\nRecommendations for Investors and Startup Founders:")
print("1. Focus on top-performing sectors like {}, which attract the most funding.".format(top_sectors.index[0]))
print("2. Cities like {} are hotspots for startups.".format(top_cities.index[0]))
print("3. Investment types like {} dominate, consider aligning strategies accordingly.".format(df['investmentntype'].mode()[0]))
print("4. Investors should monitor funding trends and target periods of high activity.")