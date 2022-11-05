import requests
import sys
import time

def getData(title, url):
    res = requests.get(url)
    
    if(res.status_code == 200):
        print(f'{title} get success')
    else:
        print(f'{title} get fail{response.status_code} {response.text}')
        sys.exit()
    # print(res.text)
    return res.json()

def postData(title, url,jData):
    response = requests.post(url, json=jData)
    if(response.status_code == 200):
        print(f"{title} send success")
    else:
        print(f"{title} send fail{response.status_code} {response.text}")
        sys.exit()
    return response

def firstConnect(ip, name):
    url = 'http://' + ip + ':8000'
    usersURL = url+ '/users'
    
    #check in
    request_body = {"user_name": ""}
    request_body["user_name"] = name
    res = postData("check in",usersURL,request_body)

    # find my name and ID
    res = getData("find my name", usersURL)
    mynum = -1
    for i,user in enumerate(res):
        if(user["name"] == name):
            print(f'the ID is {user["id"]}')
            mynum = i
    if(mynum == -1):
        print("can't find name")
        sys.exit()
    myinfo = res[mynum]

    # first connect to mypage 
    myURL = url + "/users/" + myinfo["id"]
    return myURL, myinfo["id"]

def roomiDtoURL(roomiD,ip):
    url = 'http://' + ip + ':8000'
    roomURL = url + "/rooms/" + roomiD
    return roomURL

def checkSta(myURL, roomiD):
    isStart = False
    data = getData("checkSta", myURL)
    if(data["status"] ):
        isStart = True
        roomiD = data["status"]
    return isStart,roomiD

def isBlack(roomURL ,iD):
    data = getData("is black?", roomURL)
    if(data["black"]["id"] == iD):
        return True
    else:
        return False

def getPlate(roomURL, iD):
    myTurn = False
    while(not myTurn):
        data = getData("get plate", roomURL)
        if(data["next"] == None):
            return False
        if(iD == data["next"]["id"]):
            print('my turn')
            myTurn = True
        else:
            print('waiting...')
            time.sleep(0.2)
    plate = data["board"]
    return plate

def sendNext(roomURL, iD, x,y):
    send = {"row": 0, "column": 0, "user_id": ""}
    send["user_id"] = iD

    send["row"] = y
    send["column"] = x
    postData("send put place", roomURL, send)
    return

def isAllCovered(roomURL):
    data = getData("get plate", roomURL)
    if(None ==  data["next"]):
        return True
    else:
        return False