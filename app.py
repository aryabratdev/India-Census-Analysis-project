import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title="Startup Analysis")
df = pd.read_csv('startup_cleaned (1).csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
def load_overall_analysis():
    st.title('Overall analysis')

    # total invested amount
    total=round(df["amount"].sum())

    # max amount invested in startup
    max_fun=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding=df.groupby('startup')['amount'].sum().mean()
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Total', str(total) + "Cr")
    with col2:
        st.metric('Max', str(max_fun) + "Cr")
    with col3:
        st.metric('Average',str(round(avg_funding))+"Cr")
def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 invesment of the investor
    last5_df=df[df['investors'].str.contains(investor)].head()[["date","startup","vertical","city","round","amount"]]
    st.subheader("Most Recent Invesments")
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
    #Biggest invesments
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')["amount"].sum().sort_values(ascending=False).head()
        st.subheader("Bigest Invesments")
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Sector Invested")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index,autopct="0%.01f%%")
        st.pyplot(fig1)

        df['year'] = df['date'].dt.year
        year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader("YoY Investment")
        fig2, ax2 = plt.subplots()
        ax2.histplot(year_series.index, year_series.values)
        st.pyplot(fig2)
st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox('Select one ',['Overall Analysis','Startup','Invester'])
if option == 'Overall Analysis':
    # st.title("Overall Analysis")
    bt0 = st.sidebar.button("Show Overall Analysis")
    if bt0:
        load_overall_analysis()
elif option == 'Startup':
    st.sidebar.selectbox("Select investor", sorted(df["startup"].unique().tolist()))
    bt1 = st.sidebar.button("Find The Startup Details")
    st.title("Startup Analysis")
else:
    selected_investor = st.sidebar.selectbox('Select Startup ', sorted(set(df['investors'].str.split(',').sum())))
    bt2 = st.sidebar.button("Find Investor Details")
    if bt2:
        load_investor_details(selected_investor)
