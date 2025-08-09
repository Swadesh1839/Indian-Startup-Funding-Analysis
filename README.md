# Indian-Startup-Funding-Analysis
# Startup Funding Analysis

## 📌 Overview

This Python script analyzes a dataset of startup funding rounds to uncover insights such as:

* Funding trends over time
* Top-performing sectors and cities
* Leading startups and active investors
* Distribution of investment types

It also provides **visualizations** and **recommendations** for investors and startup founders based on the data.

---

## 📂 Dataset

The script expects a CSV file named **`startup_funding.csv`** located at:

```
/content/startup_funding.csv
```

### Expected Columns:

* `Date` – Date of the funding round
* `Startup Name` – Name of the startup
* `Industry Vertical` – Sector of the startup
* `City/Location` – City where the startup is based
* `Investors Name` – Name(s) of the investors
* `InvestmentnType` – Type of investment round (Seed, Series A, etc.)
* `Amount in USD` – Funding amount in USD

---

## ⚙️ How It Works

1. **Load & Inspect Data**

   * Reads the CSV file into a pandas DataFrame
   * Prints a preview and basic info

2. **Data Cleaning**

   * Standardizes column names
   * Converts `Date` to `datetime`
   * Handles missing values
   * Cleans and converts funding amounts to numeric values
   * Standardizes investment type names

3. **Data Analysis & Visualization**

   * Funding trends over time (line chart)
   * Top 10 sectors by number of fundings (bar chart)
   * Top 10 cities by number of fundings (bar chart)
   * Top 10 startups by funding count (bar chart)
   * Top 10 active investors (bar chart)
   * Top 10 investment types (bar chart)

4. **Recommendations**

   * Identifies top-performing sectors
   * Highlights startup hotspots
   * Suggests popular investment types

---

## 📊 Example Outputs

* **Line chart** showing funding trends over time
* **Bar charts** for top sectors, cities, startups, and investors
* **Investment type distribution** visualization

---

## ▶️ Usage

1. Install required dependencies:

```bash
pip install pandas matplotlib seaborn
```

2. Place your dataset at `/content/startup_funding.csv`

3. Run the script:

```bash
python main.py
```

---

## 🛠 Dependencies

* Python 3.x
* pandas
* matplotlib
* seaborn

---

## 📌 Notes

* Ensure your CSV file has the correct column names and formatting.
* The script is currently set to run in a local or Colab-like environment (`/content/` path).
* Modify the dataset path in the code if running elsewhere.




