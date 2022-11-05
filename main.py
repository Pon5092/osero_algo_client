import osero
import com
import time

ip = '127.0.0.1'
name = 'Pon'

print('start connect')
# 最初に通信して自分の情報を登録する.
# 返り値は自分のステータス確認できるURL
myURL, iD = com.firstConnect(ip, name)
print('connect complete')
roomiD = None
while(True):
    time.sleep(1)
    #自分の現在の状態確認
    # isSrartが自分が割り振られたかどうか　RoomURLがその時のアドレス
    isStart = False
    while(not isStart):
        isStart, roomiD = com.checkSta(myURL, roomiD)
        print('waiting for challenger...')
        time.sleep(1)
    roomURL = com.roomiDtoURL(roomiD,ip)
    print(f'{roomURL=}')
    if(isStart):
        turn =0
        isEnd = False
        print('game start')
        isBlack = com.isBlack(roomURL,iD)
        while(not isEnd):
            if(com.isAllCovered(roomURL)):
                isEnd = True
                break
            #現在の盤を確認，自分の番になるまで待機
            plate = com.getPlate(roomURL,iD)
            #強制停止
            if(not plate):
                print("I can't do more")
                isEnd = True
                break
            #加工して扱いやすくする 1 = mine, -1 = yours
            plate = osero.change(plate,isBlack)
            if(not plate):
                print("I can't do more")
                isEnd = True
                break
            print('plate get =')
            for i in plate:
                print(i)
            #次の手を模索する
            y ,x, send= osero.nextWay(plate, turn)
            if(x == -1):
                print("finding ERROR: NO PUT POINTS")
                isEnd = True
                break
            print('send board =')
            for i in send:
                print(i)
            #次の手を送信存，存在しない場合(-1,-1)はデータを送らないでエラー文を出す．
            com.sendNext(roomURL, iD, x, y)

            turn +=1
            time.sleep(0.2)
            if(com.isAllCovered(roomURL)):
                isEnd = True
                break

        print('end game')
    else:
        print('waiting game to start')
        time.sleep(1.5)
