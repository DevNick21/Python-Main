import requests

res = requests.get("https://api.agify.io?name=nick")
res.raise_for_status()
data = res.json()
age = data["age"]
