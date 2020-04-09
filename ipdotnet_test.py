import random
import time
import ipdb

t0 = time.time()
db = ipdb.City("/usr/local/opt/mtr/ipdotnet.ipdb")

qty = 100000
t1 = time.time()


print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())


print(db.find("223.5.5.5","CN"))
print(db.find_map("2001:250:200::","CN"))
print(db.find_map("240C::6666","CN"))
print(db.find_map("2606:4700:4700::1111","CN"))
print(db.find_map("223.5.5.5","CN"))
print(db.find_map("8.8.8.8","CN"))
print(db.find_map(b"8.8.8.8","CN"))
print(db.find_map(b"\x08\x08\x08\x08","CN"))
print(db.find_map(0x08080808,"CN"))
print("Load: %.06fs   Used: %.07fs  QPS: %.0f/s" % (t1-t0,time.time()-t1,qty/(time.time()-t1)))
print(time.time()-t1)
