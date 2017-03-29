#!/usr/bin/env python
#import re
from __future__ import print_function
import socket, select
import threading
from flask import Flask, request, render_template, jsonify
#import queue


TS = 0
IX = 0
IY = 0
IZ = 0
U1 = 0
L1 = 0
KH = 0
KV = 0
ST = 0
BP = 0
BT = 0
BA = 0
GA = 0
GO = 0
GH = 0
GV = 0
GS = 0
FY = 0
FP = 0
FR = 0
FT = 0
TE = 0

app = Flask(__name__)
#app.config['SERVER_NAME'] = "127.0.0.1:1234"
#app.config['DEBUG'] = True

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sensors')
def interactive():
  return render_template('interactive.html')

@app.route('/background_process')
def background_process():
  try:
    return jsonify(TS=TS, IX=IX, IY=IY, IZ=IZ, U1=U1, L1=L1, KH=KH, KV=KV, ST=ST, BP=BP, BT=BT, BA=BA, GA=GA, GO=GO, GH=GH, GV=GV, GS=GS, FY=FY, FP=FP, FR=FR, FT=FT, TE=TE)
  except Exception as e:
    return str(e)


#connect to client via websockets
#send request or update automatically periodically

#access updated global variables from other thread
#no need for queue since python has a thread system for this... explain this properly


#buffer = queue.Queue(1024)


def udp(): #removed buffer arg
  global TS
  global IX
  global IY
  global IZ
  global U1
  global L1
  global KH
  global KV
  global ST
  global BP
  global BT
  global BA
  global GA
  global GO
  global GH
  global GV
  global GS
  global FY
  global FP
  global FR
  global FT
  global TE
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet and # UDP
  #if sock.bind(("",UDP_PORT)) means it listens on port 5005 to all ip addresses on the system
  sock.bind(('<broadcast>', 6000)) #
  #sock.setblocking(0)

  # while True:
  #   result = select.select([sock],[],[])
  #   msg = result[0][0].recv(1024) 
  #   print (msg)

  while 1:
    data, addr = sock.recvfrom(1024)
    print(data.decode())
   
    #print("received message: ", data.decode().split("\t"))
    #print("non split data: ", data)

    TS = ((data.decode().split("\t"))[0].split(":"))[1]
    IX = ((data.decode().split("\t"))[1].split(":"))[1]
    IY = ((data.decode().split("\t"))[2].split(":"))[1]
    IZ = ((data.decode().split("\t"))[3].split(":"))[1]
    U1 = ((data.decode().split("\t"))[4].split(":"))[1]
    L1 = ((data.decode().split("\t"))[5].split(":"))[1]
    KH = ((data.decode().split("\t"))[6].split(":"))[1]
    KV = ((data.decode().split("\t"))[7].split(":"))[1]
    ST = ((data.decode().split("\t"))[8].split(":"))[1]
    BP = ((data.decode().split("\t"))[9].split(":"))[1]
    BT = ((data.decode().split("\t"))[10].split(":"))[1]
    BA = ((data.decode().split("\t"))[11].split(":"))[1]
    GA = ((data.decode().split("\t"))[12].split(":"))[1]
    GO = ((data.decode().split("\t"))[13].split(":"))[1]
    GH = ((data.decode().split("\t"))[14].split(":"))[1]
    GV = ((data.decode().split("\t"))[15].split(":"))[1]
    GS = ((data.decode().split("\t"))[16].split(":"))[1]
    FY = ((data.decode().split("\t"))[17].split(":"))[1]
    FP = ((data.decode().split("\t"))[18].split(":"))[1]
    FR = ((data.decode().split("\t"))[19].split(":"))[1]
    FT = ((data.decode().split("\t"))[20].split(":"))[1]
    TE = ((data.decode().split("\t"))[21].split(":"))[1]

    #print ("U1 is: ", U1)

      
      #buffer.put(data.decode().split("\t"))
      #print(buffer.qsize())

    # socksend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socksend.sendto(data, ("127.0.0.1", 5005))
    # print ("message:", data)

#print (U1)

def printVar():
  threading.Timer(1.0, printVar).start()
  print("U1 is: ", U1)
  print("L1 is: ", L1)
  print("KH is: ", KH)
  print("KV is: ", KV)
  print("ST is: ", ST)
  print("GA is: ", GA)
  print("GO is: ", GO)
  print("GH is: ", GH)
  print("GV is: ", GV)
  print("GS is: ", GS)

if __name__ == '__main__':
  #global U1
  threading.Thread(target=udp).start() #removed ', args=(buffer)''
  #print ("U1 is: ", U1)
  #printVar()

  # mythread = Athread()
  # mythread.start()
  app.run()
  #app.run(host='127.0.0.1', port=1234)
