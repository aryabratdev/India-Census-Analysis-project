
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='World wide Startup Funding Analysis ')
df = pd.read_csv('Worldwide-Unicorn-Companycleaned.csv ')
# data cleaning
# df['Select Investors'] = df['Select Investors'].fillna('undisclosed')
def load_inves_analisis(investor):
    st.title(investor)
    #load the recent five inves
    last_v=df[df['investor'].str.contains(investor)].head()[["Company",'date',"Country","Industry",'Valuation']]
    st.subheader("Most Recent Inves")
    st.dataframe(last_v)
st.sidebar.title("World Wide Startup Funding Analysis")
op = st.sidebar.selectbox("Select one ",['Overall Analysis','Startup','investor'])

if op == 'Overall Analysis':
    st.title('Overall Analysis')
    bt = st.sidebar.button('Find Overall Analysis ')
elif op == 'Startup':
    st.sidebar.selectbox("Select Startup",sorted(df['Company'].unique().tolist()))
    st.title('startup Analysis')
    bt1 = st.sidebar.button('Find startup Analysis ')

else:
    select_inves=st.sidebar.selectbox("Select Investor",sorted(set(df['investor'].str.split(",").sum())))
    # st.title('investor Analysis')
    bt2 = st.sidebar.button('Find investor Analysis ')
    if bt2:
        load_inves_analisis(select_inves)

