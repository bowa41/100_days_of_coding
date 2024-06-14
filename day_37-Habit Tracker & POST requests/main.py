import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "bowa41"
TOKEN = "ljsdfJKSDFJ#$JKFDGJO%$^YRERSLDJ"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

###Create User account via POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


###Create a new graph account via POST
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Minutes Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

###Create a new pixel of data
data_endpoint= f"{graph_endpoint}/{GRAPH_ID}"
today = (datetime.today().strftime('%Y%m%d'))


pixel_data = {
    "date": "today",
    "quantity": input("How many minutes did you code today?"),
}

response = requests.post(url=data_endpoint, json=pixel_data, headers=headers)
print(response.text)

###Update a data point
UPDATE_ENDPOINT = f"{graph_endpoint}/{GRAPH_ID}/20240613"

pixel_update_data = {
    "quantity": "40"
}

# response = requests.put(url=UPDATE_ENDPOINT, json=pixel_update_data, headers=headers)
# print(response.text)

###Deleting a pixel of data
DELETE_ENDPOINT = f"{graph_endpoint}/{GRAPH_ID}/20240613"

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)