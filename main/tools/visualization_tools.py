from plotly.subplots import make_subplots
import plotly.graph_objects as go

from tools.data_tools import preparing_data_plot


def plot_baseline_price(baseline_dataset):
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
                                x=baseline_dataset['Date'],
                                open=baseline_dataset['Open'],
                                high=baseline_dataset['High'],
                                low=baseline_dataset['Low'],
                                close=baseline_dataset['Close'],
                                name = "Baseline Series"
                                ))

    fig.update_layout(
        title="TD/TO Closing Prices",
        xaxis_title="Date",
        yaxis_title="Value",
        legend_title="Legend",
        xaxis1_rangeslider_visible=False,
        font=dict(
            family="Courier New, monospace",
            size=12,
            color="black"
        )
    )
    
    return fig

def plot_prices(results):

    tks, final_series = preparing_data_plot(results)



    fig = make_subplots(rows=3, cols=2, subplot_titles=tuple(['Baseline Series - TO_DO'] + tks))




    # 0
    idx = 0
    fig.append_trace(go.Candlestick(
                                x=final_series[idx][0]['Date'],
                                open=final_series[idx][0]['Open'],
                                high=final_series[idx][0]['High'],
                                low=final_series[idx][0]['Low'],
                                close=final_series[idx][0]['Close'],
                                name = final_series[idx][0]['Ticker_Exchange'].iloc[0]
                                ),row = 1, col = 1)
    # 1
    idx = 1
    fig.append_trace(go.Candlestick(
                                x=final_series[idx][0]['Date'],
                                open=final_series[idx][0]['Open'],
                                high=final_series[idx][0]['High'],
                                low=final_series[idx][0]['Low'],
                                close=final_series[idx][0]['Close'],
                                name = final_series[idx][0]['Ticker_Exchange'].iloc[0]
                                ),row = 2, col = 1)

    # 2
    idx = 2
    fig.append_trace(go.Candlestick(
                                x=final_series[idx][0]['Date'],
                                open=final_series[idx][0]['Open'],
                                high=final_series[idx][0]['High'],
                                low=final_series[idx][0]['Low'],
                                close=final_series[idx][0]['Close'],
                                name = final_series[idx][0]['Ticker_Exchange'].iloc[0]
                                ),row = 3, col = 1)

    # 3
    idx = 3
    fig.append_trace(go.Candlestick(
                                x=final_series[idx][0]['Date'],
                                open=final_series[idx][0]['Open'],
                                high=final_series[idx][0]['High'],
                                low=final_series[idx][0]['Low'],
                                close=final_series[idx][0]['Close'],
                                name = final_series[idx][0]['Ticker_Exchange'].iloc[0]
                                ),row = 1, col = 2)

    # 4
    idx = 4
    fig.append_trace(go.Candlestick(
                                x=final_series[idx][0]['Date'],
                                open=final_series[idx][0]['Open'],
                                high=final_series[idx][0]['High'],
                                low=final_series[idx][0]['Low'],
                                close=final_series[idx][0]['Close'],
                                name = final_series[idx][0]['Ticker_Exchange'].iloc[0]
                                ),row = 2, col = 2)


    fig.update_layout(
        title_text="Time series")

    fig.update_layout(
        xaxis1_rangeslider_visible=False,
        xaxis2_rangeslider_visible=False,
        xaxis3_rangeslider_visible=False,
        xaxis4_rangeslider_visible=False,
        xaxis5_rangeslider_visible=False,
        width=1200,
        height=1200,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        )

    # save fig

    #fig.write_html('outputs/plots/similar_prices.html')

    return fig

