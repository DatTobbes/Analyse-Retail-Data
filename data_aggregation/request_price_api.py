import requests
PRICEAPI_TOKEN = ''

request_dict = dict(source='test',
                    country='us',
                    topic='search_results',
                    key='gtin',
                    values='00885909666966',
                    token='WZWUKHCEMVYZRRANFDDNRMOPJOKJYMXGRPFHAGZXJEGMSXFXLCWQAUGZSBLHVWSE')

url='https://api.priceapi.com/v2/'

r = requests.get('https://api.priceapi.com/v2/jobs/5bca528dbbd7e5125841e512/download.json?token='+PRICEAPI_TOKEN)
print(r.status_code)
print(r.content)

r.request('POST', url=url, params= request_dict)
