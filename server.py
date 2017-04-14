#!/usr/bin/env python

from __future__ import print_function
import socket, select
import sys
import struct
import threading
import json
from flask import Flask, request, render_template, jsonify
from binascii import a2b_base64


TS = 0
IX = 24
IY = 34
IZ = 45
U1 = 5
L1 = 67
KH = 10
KV = 68
ST = 45
BP = 34
BT = 45
BA = 56
GA = 79
GO = 56
GH = 89
GV = 4
GS = 45
FY = 567
FP = 34
FR = 46
FT = 34
TE = 0
global sending
sending = 0

#******UNCOMMENT ALL BELOW**********
# def connect():
#   sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
#   s_a = ("192.168.0.2",4003) #IP and Port Number
#   print ("before bind")
#   sock1.bind(s_a)
#   print ("bind")
#   sock1.listen(1)
#   print("Waiting for Connection")
#   global connection
#   connection, c_a = sock1.accept()

# print ("pre connect")
# if sending == 0:
#   connect()
#   global sending
#   sending = 1
  
# print ("after connect")





app = Flask(__name__)




@app.route('/', methods=['GET']) 
def index():

  return render_template('index.html', U1=U1)

@app.route('/getmethod/')
def get_javascript_data():
  

  x = request.args.get("x")
  y = request.args.get("y")
  w = request.args.get("w")
  h = request.args.get("h")
  


  print (x)
  print (y)
  print (w)
  print (h)
  imagetosend = request.args.get("imagetosend")
  converted_image = a2b_base64(imagetosend)
  print (converted_image)
  #*********UNCOMMENT THIS********
  # mess = struct.pack('>I',int(x)) # Packs the int 1001 into bytes to send
  # connection.send(mess)
  # mess = struct.pack('>I',int(y))
  # connection.send(mess)
  # mess = struct.pack('>I',int(w))
  # connection.send(mess)
  # mess = struct.pack('>I',int(h))
  # connection.send(mess)
  # connection.send(converted_image)
  # connection.close()
  # sock1.close()

  return jsonify(x=x, y=y, w=w, h=h)

@app.route('/track', methods=['GET'])
def track():
  return render_template('track.html', U1=U1)

@app.route('/sensors')
def interactive():
  return render_template('interactive.html', TS=TS, IX=IX, IY=IY, IZ=IZ, U1=U1, L1=L1, KH=KH, KV=KV, ST=ST, BP=BP, BT=BT, BA=BA, GA=GA, GO=GO, GH=GH, GV=GV, GS=GS, FY=FY, FP=FP, FR=FR, FT=FT, TE=TE)

@app.route('/background_process')
def background_process():
  try:
    return jsonify(TS=TS, IX=IX, IY=IY, IZ=IZ, U1=U1, L1=L1, KH=KH, KV=KV, ST=ST, BP=BP, BT=BT, BA=BA, GA=GA, GO=GO, GH=GH, GV=GV, GS=GS, FY=FY, FP=FP, FR=FR, FT=FT, TE=TE)
  except Exception as e:
    return str(e)

@app.route('/livestream')
def livestream():
  return render_template('livestream.html')

@app.route('/map')
def map():
  return render_template('map.html')

@app.route('/about')
def about():
  return render_template('about.html')
#connect to client via websockets
#send request or update automatically periodically

#access updated global variables from other thread
#no need for queue since python has a thread system for this... explain this properly



def udp(): 
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

    
    # socksend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socksend.sendto(data, ("127.0.0.1", 5005))
    # print ("message:", data)


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
  #****threading.Thread(target=udp).start() #removed ', args=(buffer)''
  #print ("U1 is: ", U1)
  #printVar()

  # mythread = Athread()
  # mythread.start()
  #***threading.Thread(target=connect).start()
  
  print ("pre app.run")
  app.run()

  print ("after app.run")
  

  print (sending)
  #app.run(host='127.0.0.1', port=1234)





