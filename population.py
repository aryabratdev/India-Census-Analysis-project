import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("india census.csv")

list_state = list(df["State"].unique())

list_state.insert(0,'Overrall India')
st.set_page_config(layout='wide',page_title="India Census Analysis")
st.sidebar.title(" India Census Data Visualization ")

state = st.sidebar.selectbox("select state",list_state)
primary = st.sidebar.selectbox("Select primary parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select secondary parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("plot graph")

if plot:
    st.title("India Census")
    st.text("Size represents primary parameter")
    st.text("Color represents secondary parameter")

    if state == "Overrall India":
        # ploting for india
        fig=px.scatter_mapbox(df,lat='Latitude',lon="Longitude",zoom=4,size=primary,color=secondary,size_max=35,
                              mapbox_style="carto-positron",width=1200,height=700,hover_name="District")
        st.plotly_chart(fig,theme=None,use_container_width=True)
    else:
        # plot for state
        s_df = df[df["State"] == state]
        fig = px.scatter_mapbox(s_df, lat='Latitude', lon="Longitude", zoom=6, size=primary, color=secondary, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700 , hover_name="District")
        st.plotly_chart(fig, theme=None,use_container_width=True)
