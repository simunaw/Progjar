import requests

URL = "https://stackoverflow.com"

response = requests.get (URL)

open ("stackoverflow.com", "wb").write(response.content)