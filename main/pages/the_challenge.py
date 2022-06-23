from pandas import read_csv as pd_read_csv

import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS
from tools.visualization_tools import plot_baseline_price

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>The Challenge</span>", unsafe_allow_html=True)

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>Challenge Description</span>", unsafe_allow_html=True)

    st.write("The proposed challenge is basically to take a given financial series and date range and find other series with the simillar movements over time.")
    
    st.write("In sum, we need to find similarities between the given time series and any others of our choice.")

    st.write("To solve the challenge, we need to find at least 5 other series with a similarity rate equal or higher than 80%.")

    
    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>The Data</span>", unsafe_allow_html=True)

    st.write("The series is the Toronto Dominion Bank stocks negotiated in Canada, Toronto, Exchange.")
    
    st.write("The baseline period ranges between December 2021 and February 2022.")

    st.write("We can visualize the series in the following:")

    data = pd_read_csv('data/baseline_todo.csv')


    plot_figure = plot_baseline_price(data)


    st.plotly_chart(plot_figure, use_container_width=True)