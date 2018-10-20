import pandas as pd


class RetailerData:

    def __init__(self):
        self.retail_data = pd.read_csv('../data/retailer_data.csv', sep=';', encoding='ansi')

    def get_inventory(self):
        return self.retail_data

    def get_device_list(self):
        return self.retail_data['retailer_product'].values

    def get_device_from_inventory(self, item='Apple iPhone 8 Plus (64GB)'):
        df = self.retail_data.loc[self.retail_data['retailer_product'] == item]
        return df

    def get_cheapest_devices(self):
        df = self.retail_data.sort_values(by='retailer_price')
        return df.ix[1]

    def get_expensive_devices(self):
        df = self.retail_data.sort_values(by='retailer_price')
        return df.tail(1)

    def get_device_in_price_range(self, lower, upper):
        df = self.retail_data
        df = df[(df.retailer_price > lower) & (df.retailer_price < upper)]
        return df

    def get_neighbours_from_device(self, item='Apple iPhone 8 Plus (64GB)'):
        df = self.retail_data
        device = df.loc[df['retailer_product'] == item]
        price = device.retailer_price.values[0]

        tmp1 = df[df.retailer_price > price].sort_values(by='retailer_price')
        tmp1 = tmp1.head(5)

        tmp2 = df[df.retailer_price < price].sort_values(by='retailer_price')
        tmp2 = tmp2.tail(5)
        frames = [tmp1, tmp2]

        result ={

        }
        return result



if __name__ == "__main__":
    rd = RetailerData()
    # print(rd.get_inventory().head(5))
    # print(rd.get_cheapest_devices())
    # print(rd.get_device_in_price_range(500,900))
    # print(rd.get_expensive_devices())
    # print(rd.get_device_from_inventory())
    print(rd.get_neighbours_from_device())
    print(rd.get_device_list())
