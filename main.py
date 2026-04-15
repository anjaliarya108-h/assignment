import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    sentiment = pd.read_csv('fear_greed_index.csv')
    trades = pd.read_csv('historical_data.csv')

    sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce').dt.date
    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], errors='coerce')
    trades['date'] = trades['Timestamp IST'].dt.date

    merged = pd.merge(trades, sentiment, on='date', how='inner')

    merged['win'] = merged['Closed PnL'] > 0

    return merged

df = load_data()

st.sidebar.title("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

df_filtered = df[df['classification'].isin(sentiment_filter)]

st.title("Trader Behavior vs Market Sentiment")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(df_filtered))
col2.metric("Avg PnL", round(df_filtered['Closed PnL'].mean(), 2))
col3.metric("Win Rate", round(df_filtered['win'].mean(), 2))


st.subheader("PnL Distribution")

fig, ax = plt.subplots()
sns.histplot(df_filtered['Closed PnL'], bins=50, ax=ax)
st.pyplot(fig)

st.subheader("PnL by Sentiment")

fig, ax = plt.subplots()
sns.boxplot(x='classification', y='Closed PnL', data=df_filtered, ax=ax)
st.pyplot(fig)

st.subheader("Long vs Short")

direction = pd.crosstab(df_filtered['classification'], df_filtered['Side'])

st.bar_chart(direction)

st.subheader("Top Traders")

top_traders = (
    df_filtered.groupby('Account')['Closed PnL']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_traders)

if st.checkbox("Show Raw Data"):
    st.dataframe(df_filtered.head(100))