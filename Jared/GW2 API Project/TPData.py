import requests

response = requests.get(r"https://api.guildwars2.com/v2/commerce/listings")

print(response.status_code)