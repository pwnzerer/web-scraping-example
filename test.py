import requests


results = requests.get("https://well.ca/products/navitas-naturals-organic-acai-powder_99112.html")
print(results.text)