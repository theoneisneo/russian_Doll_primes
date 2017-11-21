# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import time
t1 = time.time()

def isPrime(n):
    if n < 2:
        return False
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

rdp = [2, 3, 5, 7]
add = [1, 3, 5, 7, 9]

for p in rdp:
    for a in add:
        s = 10 * p + a
        if isPrime(s):
            rdp.append(s)

t2 = time.time()

print(rdp)
print("cost time : " + str(t2 - t1))
