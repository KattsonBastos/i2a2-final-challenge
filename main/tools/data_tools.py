

def preparing_data_plot(results):
    tks = []
    tks_tmp = []

    final_series = []

    count = 0

    while len(tks) < 5:

        f_serie = results[count]
        
        count += 1

        serie_ticker = f_serie[0]['Ticker_Exchange'].iloc[0]

        if serie_ticker in tks_tmp:

            continue
        
        tks.append(serie_ticker + f" - Similarity: {round(f_serie[1]*100, 2)}%")
        tks_tmp.append(serie_ticker)
        final_series.append(f_serie)

    return tks, final_series
