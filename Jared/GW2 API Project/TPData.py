import requests, json, time
import pandas as pd 
from os import system

clear = lambda: system('cls')

while True:
    clear()
    date = time.strftime("%m/%d/%y %H:%M")
    response = requests.get(r"https://api.guildwars2.com/v2/commerce/listings/19721.json")
    json_data = json.loads(response.text)

    buys = pd.DataFrame.from_dict(json_data["buys"], orient='columns')
    sells = pd.DataFrame.from_dict(json_data["sells"], orient='columns')

    data_buys = buys.describe()['unit_price']
    data_sells = sells.describe()['unit_price']

    frames = [data_buys, data_sells]
    new_index = ['Buy', 'Sell']

    result = pd.concat(frames, axis=1).T
    result.reset_index(inplace=True, drop=True)
    result['Type'] = new_index
    result['Date'] = date

    result.to_csv('Globs.csv', mode='a', header=False, index=False)
    print(f"\nUpdate Completed @ {date}")
    time.sleep(60)