import requests
from datetime import datetime as dt

USERNAME = "klaus"
TOKEN = "firsttoekeane"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofservice": "yes",
    "notMinor": "yes",

}

# res = requests.post(url=pixela_endpoint, json=user_params)
# print(res.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": ID,
    "name": "coding graph",
    "unit": "days",
    "type": "int",
    "color": "momiji"

}
headers = {"X-USER-TOKEN": TOKEN}


# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)

today = dt.now()

pixel_endpoint = f"{graph_endpoint}/{ID}"
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4",
}

# res = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

# print(res.text)


update_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_pixel_params = {
    "quantity": "30", }

# res = requests.put(url=update_pixel_endpoint,
#                    json=update_pixel_params, headers=headers)

# print(res.text)
delete_pixel_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

res = requests.delete(url=delete_pixel_endpoint, headers=headers)

print(res.text)
