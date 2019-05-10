import network
import ubinascii

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
a=wlan.scan()
print("List of all Access points around......")
for e in a:
    b=e[1]
    c=ubinascii.hexlify(b)
    d=c.decode('utf-8')
    print(e[0]+"Their mac Address is:"+str(d))
