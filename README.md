# assignment

**Overview**
This project analyzes how market sentiment (Fear vs Greed) impacts trader behavior and performance on Hyperliquid.
The goal is to uncover patterns that can help design smarter trading strategies.

**Objective**
Understand the relationship between Bitcoin market sentiment and trader performance
Identify behavioral patterns across different trader segments
Generate actionable insights for improving trading strategies
Build a simple model to predict next-day profitability
**Dataset Description**
1. Bitcoin Market Sentiment Dataset
Columns:
date
classification (Fear / Greed / Extreme Fear)
2. Historical Trader Data (Hyperliquid)
Key columns:
Account
Execution Price
Size USD
Side (Buy/Sell)
Timestamp IST
Closed PnL
**Tech Stack** 
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn
**How to Run**
Clone the repository:
git clone https://github.com/your-username/project-name.git
cd project-name
Install dependencies:
pip install -r requirements.txt
Run the notebook:
jupyter notebook
**Project Structure**
├── data/
│   ├── sentiment.csv
│   ├── trades.csv
├── untitled.ipynb
├── README.md
├── requirements.txt
