import pandas as pd
import numpy as np

class DataFrameReader:

    def __init__(self):
        hist_data = pd.read_csv('../data/device_hist_price.csv', sep='\t')
        recomm_data= pd.read_csv('../data/product_recommendation.csv', sep=';', encoding='ansi')
        shop_data = pd.read_csv('../data/productvariation.csv', sep=';', encoding='ansi')


        df = pd.merge(hist_data, recomm_data, how='inner', on=None, left_on='name', right_on='product name',
                 left_index=False, right_index=False, sort=True,
                 suffixes=('_x', '_y'), copy=True, indicator=False,
                 validate=None)
        self.df = df.dropna()
        self.df.drop(columns=['product name'])

    def get_min_prices(self,df,item='Apple iPhone 7 Plus (32GB)'):

        df= df.loc[df['name']==item]
        min_prices = df.iloc[:, 2:30].values
        return min_prices[0]

    def get_max_prices(self,df ,item='Apple iPhone 7 Plus (32GB)'):

        df= df.loc[df['name']==item]
        min_prices = df.iloc[:, 30:58].values
        return min_prices[0]

    def get_availability(self,df ,item='Apple iPhone 7 Plus (32GB)'):

        df= df.loc[df['name']==item]
        availability = df.iloc[:, 58:86].values
        return availability[0]

    def get_recommendations(self, df, item='Apple iPhone 7 Plus (32GB)'):
        df = df.loc[df['name'] == item]
        recommmendation = df.iloc[:, -4:].values
        return recommmendation[0]

    def get_stars(self, df, item='Apple iPhone 7 Plus (32GB)'):
        df = df.loc[df['name'] == item]
        stars = df.iloc[:, -7].values
        return stars[0]

    def get_people_rating(self, df, item='Apple iPhone 7 Plus (32GB)'):
        df = df.loc[df['name'] == item]
        people_rating = df.iloc[:, -8].values
        return people_rating[0]


    def create_device_data(self,  item='Apple iPhone 7 Plus (32GB)'):
        min_prices = self.get_min_prices(self.df, item)
        max_prices = self.get_max_prices(self.df, item)
        availability = self.get_availability(self.df, item,)

        recommendations= self.get_recommendations(self.df, item)
        stars = self.get_stars(self.df, item)
        people_rating = self.get_people_rating(self.df, item)

        device_dict = {
            'min_prices': min_prices.tolist(),
            'max_prices': max_prices.tolist(),
            'availability': availability.tolist(),
            'recommendations': recommendations.tolist(),
            'stars': stars,
            'people_rating': people_rating.tolist()
        }
        return device_dict
