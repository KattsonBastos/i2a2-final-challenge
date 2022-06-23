import streamlit as st
from pandas import read_csv as pd_read_csv
import streamlit.components.v1 as components

from tools.visualization_tools import plot_baseline_price
from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>Implementation and Results</span>", unsafe_allow_html=True)


    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>Project Requirements</span>", unsafe_allow_html=True)
    st.markdown("First of all, these are the project dependencies:")
    
    code = ''' 
fastparquet==0.8.1
matplotlib==3.5.2
numpy==1.22.4
pandas==1.4.2
plotly==5.8.0
tqdm==4.64.0
    '''
    st.code(code, language='python')

    st.markdown("Since we get them installed, we can import them.")

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>0. Importing Modules</span>", unsafe_allow_html=True)

    st.markdown(f"The following packages are going to be using during the entire implementation:", unsafe_allow_html=True)

    code = """
    import random

import numpy                  as np
import pandas                 as pd
import matplotlib.pyplot      as plt
import plotly.graph_objects   as go

from tqdm                     import tqdm
from fastparquet              import ParquetFile
from plotly.subplots          import make_subplots"""

    st.code(code, language='python')

    st.markdown(f"We are also going to define some functions which are going to help us.", unsafe_allow_html=True)


    code = """def min_max_scaler(x_vector):
    '''
    Receives a numpy array and return it scaled by its min and max values.
    :params x_vector: a numpy array of 1 dimension.
    returns: numpy array with the scaled values.
    '''

    return np.array([(x - np.min(x_vector)) / (np.max(x_vector) - np.min(x_vector)) for x in x_vector])
    
    """

    st.code(code, language='python')

    st.markdown("The above function is going to be used to scale series with the Min Max method. <br> <br>\
        In order to calculate the area and get the similarity rate, we're going to use the following function:", unsafe_allow_html=True)

    code = """def calculate_auc(v1, v2, total_area):
    '''
    receives two numpy arrays of same length, calculate the area between them and return that area over the total area.
    :params v1, v2: numpy arrays of 1 dimension
    returns: float percentage (decimal) of the area between the two curves over the total area.
    '''

    x = np.array(range(len(v1)))
    z = v1-v2
    dx = x[1:] - x[:-1]

    cross_test = np.sign(z[:-1] * z[1:])

    dx_intersect = - dx / (z[1:] - z[:-1]) * z[:-1]

    areas_pos = abs(z[:-1] + z[1:]) * 0.5 * dx

    areas_neg = 0.5 * dx_intersect * abs(z[:-1]) + 0.5 * (dx - dx_intersect) * abs(z[1:])

    areas = np.where(cross_test < 0, areas_neg, areas_pos)

    area_proportion = np.sum(np.abs(areas)) / total_area

    return 1 - area_proportion
    """

    st.code(code, language='python')

    st.markdown("We are also going to make the use of the following function to get the area under an entire curve:")

    code = """def get_auc(y):

    auc = np.trapz(y=y, x=list(range(len(y))))

    return auc    
    """

    st.code(code, language='python')

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>1. Loading Data</span>", unsafe_allow_html=True)

    st.markdown("The given dataset is loading in the snippet bellow. It's in the Parquet Format.")

    code = """data = ParquetFile(BASE_PATH + 'database.parquet').to_pandas()"""

    st.code(code, language='python')

    st.markdown("The data looks like the following:")

    st.image("images/data_head.png")

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>2. Data Understanding and Preparation</span>", unsafe_allow_html=True)

    st.markdown("In order to get the right Ticker, the right stock data from the right Exchange, we're going to create a new column \
        joining the Stock Ticker and the Exchange it's negotiated:")
    
    code = """data['Ticker_Exchange'] = data['Ticker'] + '_' + data['Exchange']"""

    st.code(code, language='python')

    st.markdown("Since our Ticker is the Toronto Dominion Bank negotiated in the Toronto Exchange, Canada, \
        we'll save it in a separate variable to be later used in the area comparison. We're also going to filter the target date period.")

    code = """data_TODO = data[data['Ticker_Exchange'] == 'TD_TO']

baseline_TODO = data_TODO[(data_TODO['Date'] >= '2021-12-01') & (data_TODO['Date'] <= '2022-02-01')]"""

    st.code(code, language='python')

    st.markdown("Before we start the implementation, we are going to create a list with all unique Ticker-Exchange pairs, so we can later iterate over them and filter its data from our dataset. \
        <br>The following snippet does that:")

    code = """tickers = list(data['Ticker_Exchange'].unique())"""

    st.code(code, language='python')

    st.markdown("Since we don't want to find a similar period in the Toronto Dominion Bank negotiated in Toronto Exchange, \
        we'll remove it from the list: ")
    
    code = """tickers.remove('TD_TO')"""

    st.code(code, language='python')

    st.markdown("With that in hand, we already have everything we need to start the implementation.")

    st.markdown("We have a total of 8,931 unique Ticker-Exchange pairs in our list.")

    st.markdown("So, let's take a better look at our baseline data, the Toronto Dominion Bank?")

    st.markdown("The period has a length of 42 days, going from december 1st, 2021, to february 1st, 2022.<br><br>\
        We can visualize it in the following plot (data not scaled):")

    data = pd_read_csv('data/baseline_todo.csv')

    plot_figure = plot_baseline_price(data)


    st.plotly_chart(plot_figure, use_container_width=True)


    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>3. Implementation</span>", unsafe_allow_html=True)

    st.markdown("First, we'll apply that Min Max function to get the data in the range of 0 to 1 and make them comparable.")

    code = """series = min_max_scaler(baseline_TODO['Close'].values)"""

    st.code(code, language='python')

    st.markdown("The whole 'finder algorithm' is inside the following snippet. First, we set a random seed to ensure the reproducibility and then \
        create  list to store the results. We also create a variable *N* representing the size of Ticker-Exchange pairs we want.")
    
    code = """random.seed(11)

results = []

N = 200

for ticker in tqdm(random.sample(tickers, N)):

    target_series = data[data['Ticker_Exchange'] == ticker]

    for i in range(target_series.shape[0]):

        tmp_data = target_series.iloc[i:i+len(series), :].reset_index(drop=True)
        
        if tmp_data.shape[0] != len(series):

            continue

        tmp_series = min_max_scaler(tmp_data['Close'].values)  
        r_plus = np.array([i if i > j else j for i,j in zip(series, tmp_series)])

        total_area = get_auc(r_plus)

        output = calculate_auc(series, tmp_series, total_area)

        if  output >= .80:
            results.append((tmp_data, output))"""

    st.code(code, language='python')

    st.markdown("In the following, we start a loop over a sample of the tickers list, filtering the data corresponding to the iteration ticker. \
        In the sequence, we start another loop, but this time it is over the target series, walking through it and getting a slice in the length of the baseline one, that is, 42. \
            <br>After that, we bring the series to the range of 0 to 1 and calculate the area between the baseline and the target series, getting the similarity coefficient. \
                To do that we use helper function we saw at the beginning of this section. We also pass to the function the total area of both curves. This way, if the similarity is above 80%, we add the series to the pre-defined result list.", unsafe_allow_html=True)
     

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>4. Results</span>", unsafe_allow_html=True)

    st.markdown("We ended with a result's length of 6,879 series with a similarity coefficient higher than 80%.")

    st.markdown("The following figure shows the baseline series, *TD_TO*, and the top 5 series by similarity. \
        It's clear that the adopted strategy can't get perfectly the similarity between series, \
            but it's fitting for this first project cycle. The method captured the oscillations reasonably well, \
                even though a human analysis could say that *NEM_NYSE* series doesn't seem to have a similarity \
                    higher than *BTA_NYSE*. That's a point we'll have to work on in the next cycle.")
    

    st.markdown("### Baseline and Similar Series")

    HtmlFile = open("outputs/plots/results.html", 'r')
    source_code = HtmlFile.read() 
    components.html(source_code, width= 800, height = 1200)