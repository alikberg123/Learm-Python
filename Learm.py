import time

a = 0
player = True
while player:
    time.sleep(2)
    a += 1
    if a >= 5:
        player = False
    print(a)
