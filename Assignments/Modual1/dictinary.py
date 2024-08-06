import requests
url="https://data.covid19india.org/data.json"

req=requests.get(url)
data=req.json()
#print(data["statewise"])

for i in data["statewise"]:
    print(f"State name: {i["state"]}")
    print(f"Confirmed: {i["confirmed"]}")
    print(f"Deathes: {i["deaths"]}")