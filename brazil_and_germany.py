import math as mt


try:
    while True:
        n = int(input())
        if n==0: break
        br = mt.floor(n / 90)
        gr = mt.ceil(7 * n / 90)
        print(f"Brasil {br} x Alemanha {gr}")
except:
    pass
