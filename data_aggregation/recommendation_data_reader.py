import pandas as pd
from data_aggregation.shop_price_data import ShopDataReader
from data_aggregation.read_price_data import HistoricalPriceDataReader


class RecomondationReader:

    def __init__(self, path='../data/product_recommendation.csv'):
        self.df = pd.read_csv(path, sep=';', encoding='ansi')
        self.df.drop(columns=['recommendation 1'])
        self.shop_data = ShopDataReader()
        self.historical_data = HistoricalPriceDataReader()

    def get_recommendations(self, device):

        df= self.df.loc[self.df['product name'] == device]
        return df


if __name__ == "__main__":
    r = RecomondationReader()
    print(r.get_recommendations('Xiaomi Redmi Note 5 (64GB)'))

