import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, ColorBar, Range1d, LabelSet, Label
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
from bokeh.models import BoxAnnotation


class ShopDataReader:

    def __init__(self, path='../data/productvariation.csv'):
        self.df = pd.read_csv(path, sep=';', encoding='ansi')
        self.df = self.aggregate()

    def aggregate(self, columns=['product', 'price', 'shop']):
        return pd.DataFrame(data=self.df[columns])

    def select_items(self, item='Samsung Galaxy S8 (64GB)'):
        df = self.df.loc[self.df['product'] == item]
        return df

    def plot_cheapest_shops(self, df, n=10):
        df = df.reindex()
        y = np.asarray(df.groupby(['shop']).price.min().values, dtype=np.float32)
        x = df.index
        mid_prices, upper_range, lower_range = self.get_price_range(df)

        mapper = linear_cmap(field_name='y', palette=Spectral6, low=min(y), high=max(y))

        p = figure(plot_width=500, plot_height=500, title="")

        color_bar = ColorBar(color_mapper=mapper['transform'], width=8, location=(0, 0))


        mid_box = BoxAnnotation(bottom=lower_range, top=upper_range, fill_alpha=0.1, fill_color='green')

        p.add_layout(mid_box)

        p.y_range = Range1d(0, max(y))
        p.add_layout(color_bar, 'right')
        p.scatter(x=x[:n], y=y[:n], line_color=mapper, color=mapper, fill_alpha=1, size=12)
        output_file("scatter.html")
        show(p)

    def get_price_range(self, df, p_range=0.1):
        prices = np.asarray(df['price'].values, dtype=np.float32)
        range = max(prices) - min(prices)
        mid_prices = range / 2 + min(prices)
        upper_range = mid_prices * (1+p_range)
        lower_range = mid_prices * (1-p_range)
        print(mid_prices, upper_range, lower_range)
        return mid_prices, upper_range, lower_range


if __name__ == "__main__":
    sh = ShopDataReader()
    print(sh.aggregate())
    sh.get_price_range(sh.select_items())
    sh.plot_cheapest_shops(sh.select_items())
