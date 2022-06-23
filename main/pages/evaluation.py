import streamlit.components.v1 as components
import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>Strategy Evaluation</span>", unsafe_allow_html=True)
    
    st.markdown("For this first cycle, we'll perform two generalization tests: ")

    st.markdown("* Test 1: test a different Ticker-Exchange pair, but with the same period length, that is, 42 days;")
    st.markdown("* Test 2: test a different Ticker-Exchange pair, but with a priod of 1 (one) year.")

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>Testing Generalization 1: BIT_NYSE with a period of 42 days</span>", unsafe_allow_html=True)

    st.markdown("For this first generalization test, we randomly selected the BIT_NYSE to be our baseline series. The implementation was the same: apply the min max scaling function and iterate over the tickers.")

    st.markdown("The result is as follows: ")


    HtmlFile = open("outputs/plots/generalization1.html", 'r')
    source_code = HtmlFile.read() 
    components.html(source_code, width= 800, height = 1200)

    st.markdown("As before, the implemented technique was able to capture the overall movements of the series, identifying series which seems to really have some similarity with the baseline.", unsafe_allow_html=True)


    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>Testing Generalization 2: TCPC_NASDAQ with a period of 1 year</span>", unsafe_allow_html=True)

    st.markdown("For this second test, we randomly selected the TCPC_NASDAQ ticker and followed the same implementation.")

    st.markdown("Since we're now dealing with a higher period, we decrease the number of target tickers from 200 to 100 in order to save some processing time.")

    HtmlFile = open("outputs/plots/generalization2.html", 'r')
    source_code = HtmlFile.read() 
    components.html(source_code, width= 800, height = 1200)

    st.markdown("The strategy had a little trouble finding similar series, since, with a visual analysis, we can see some differences between the series. However, it still could capture some tendency movements.")

    st.markdown("These latest results indicates we still have to work on our strategy.")