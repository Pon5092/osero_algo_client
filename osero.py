import numpy as np
import math
import random
import sys

def arange(plate, a,b):
  # 1 = black 2 = white
  for i in range(len(plate)):
    for j in range(len(plate[0])):
      if(plate[i][j] ==1):
        plate[i][j]= a
      elif(plate[i][j] == 2):
        plate[i][j] = b
  return plate

def change(plate, isBlack):
  if(isBlack):
    plate = arange(plate, 1, -1)    
  else:
    plate = arange(plate, -1, 1)
  return plate

def check(plate,x,y,size,isChosen):
  #　そこに置かれた場合どうなるか確認する
  # 0 = no flipts or can't put, else = flip num
  if(plate[y][x] != 0):
    return 0
  lookway = np.array([[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]])

  check_isfold = False
  fold_num = 0
  for way in lookway:
    go = False
    x_now = x + way[0]
    if(0 > x_now or x_now >= size):
        continue
    y_now = y + way[1]
    if(0 > y_now or y_now >= size):
        continue
    while(plate[y_now][x_now] == -1):
      x_now += way[0]
      if(0 > x_now or x_now >= size):
        break
      y_now += way[1]
      if(0 > y_now or y_now >= size):
        break
      if(plate[y_now][x_now] == 1):
        check_isfold = True
        x_now -= way[0]
        y_now -= way[1]
        while(plate[y_now][x_now] == -1):
          fold_num += 1
          if(isChosen):
            plate[y_now][x_now] = 1
            print(f'folded {x_now},{y_now}')
          x_now -= way[0]
          y_now -= way[1]
  if(check_isfold):
    if(isChosen):
      plate[y][x] = 1
      return plate
    else:
      return fold_num
  else:
    # print("can't fold")
    return 0

def choose(plate,size,turn):
  may = []
  for x in range(size):
    for y in range(size):
      foldNum = check(plate,x,y,size,False)      
      if(foldNum != 0):
        may.append([foldNum,x,y])
  if(len(may) ==0):
    return -1,-1
  may.sort()
  may.reverse()
  print("maybe next =")
  for i in may:
    print(i)
  print()
  for i in range(15):
    for j in range(len(may) -1):
      if(may[j][0] == may[j+1][0]):
        if(random.random() > 0.2):
          may[j], may[j+1] = may[j+1], may[j]
  choosen = int(random.uniform(0,min(math.log2(size*size-turn)/2,len(may))))
  return may[choosen][2], may[choosen][1]


def nextWay(plate, turn):
  """
  #for debug
  console = input().split()
  x = int(console[0])
  y = int(console[1])
  """
  y ,x = choose(plate,len(plate),turn)
  if(x == -1):
    return -1,-1,plate
  plate = check(plate,x,y,len(plate),True)
  return y ,x, plate



