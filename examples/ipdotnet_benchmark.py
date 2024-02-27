import random
import time
import ipdb
import socket, struct

t0 = time.time()
db = ipdb.City("/usr/local/opt/mtr/ipdotnet.ipdb")

qty = 100000
t1 = time.time()
for i in range(qty):
    #db.find(random.randrange(0x20000000,0xd2000000),"CN")
    db.find(socket.inet_ntoa(struct.pack('!L', random.randrange(0x20000000,0xd2000000))),"CN")
print("Load: %.06fs   List Used: %.07fs  QPS: %.0f/s  Time/s: %.2fus" % (t1-t0,time.time()-t1,qty/(time.time()-t1),(time.time()-t1)*1000000./qty))
t1 = time.time()
for i in range(qty):
    db.find_map(random.randrange(0x20000000,0xd2000000),"CN")
print("Load: %.06fs   Map  Used: %.07fs  QPS: %.0f/s" % (t1-t0,time.time()-t1,qty/(time.time()-t1)))
print(time.time()-t1)
