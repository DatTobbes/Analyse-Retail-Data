import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show


class HistoricalPriceDataReader:

    def __init__(self, path='../data/price_data_reader.csv'):
        self.df = pd.read_csv(path, sep='\t')

    def get_historical_data_for_device(self, item="Apple iPhone 7 Plus (32GB)"):

        df  = self.df.loc[self.df['name']==item].transpose()
        df.columns=['prices']
        df = df.reset_index(drop=True)
        df = df['prices'].str.replace(',', '.')
        
        min_prices = df.iloc[2:30].values
        max_prices = df.iloc[29:57].values
        availability = df.iloc[57:85].values

        min_prices = min_prices.reset_index(drop=True)
        availability = availability.reset_index(drop=True)

        df = pd.DataFrame(
            data=[np.asarray(min_prices, dtype=np.float32),
                  np.asarray(max_prices, dtype=np.float32),
                  availability],
            dtype=np.float32)
        df = df.transpose()
        df.columns = ['min_price', 'max_price', 'availability' ]
        return df

    def plot(self, df):
        p = figure()
        p.scatter(np.asarray(df['max_price'], dtype=np.float32), np.asarray(df['ava'], dtype=np.float32),
                  fill_color="red")
        output_file("scatter.html")
        show(p)

if __name__ == "__main__":
    reader = HistoricalPriceDataReader()
    print(reader.get_historical_data_for_device())