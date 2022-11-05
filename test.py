import requests
import json
"""
roomUrl ="http://127.0.0.1:8000/rooms/363faa84-597e-4c10-9f8b-dcd95aa6590a"
send_b = { "row": 4, "column": 2,"user_id": "7f637fbb-a139-41ef-8ee5-f1fc58206b75"}
send_w = { "row": 4, "column": 2,"user_id": "ec74692d-bb78-453e-ae16-8fd6591134ff"}
send = send_w
send["row"] = 2
send["column"] = 4
response = requests.post(roomUrl, json = send)
"""

roomUrl ="http://127.0.0.1:8000/rooms"
response = requests.post(roomUrl)
print(response)

"""
res = requests.get(roomUrl)
RoomSta = res.json()
board = RoomSta["board"]
for i in board:
    print(i)
"""