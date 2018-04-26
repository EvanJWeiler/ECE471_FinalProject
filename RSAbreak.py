import math
import time

def encrypt(m, key):
    return m**key[0] % key[1]

def findNums(pubKey):
    n = pubKey[1]
    for i in range(0,n):
        #print i, n
        for j in range(0, n):
            if i * j == n and isPrime(i) and isPrime(j):
                return [i, j]
    return -1

def genPrivKey(nums, pubKey):
    e = pubKey[0]
    nPhi = (nums[0] - 1) * (nums[1] - 1)
    d = multInverse(e, nPhi)
    return [d, pubKey[1]]

def isPrime(num):
    if n < 2: return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def multInverse(e, n):
    nOrig = n
    x1, x2, y1, y2 = 1, 0, 0, 1
    while n != 0:
        c, e, n = e // n, n, e % n
        x1, x2 = x2, x1 - c * x2
        y1, y2 = y2, y1 - c * y2
    if x1 < 0:
        x1 += nOrig
    return  x1

p = 997
q = 773
n = p*q
e = 131
pubKey = [e, n]
m = 9

print "message:" , m
c = encrypt(m, pubKey)
print "cypher:" , c
nums = findNums(pubKey)
print nums
privKey = genPrivKey(nums, pubKey)
print privKey
mNew = encrypt(c, privKey)
print "decrypted message:" , mNew


######### CHECK FOR PRIME NUMBERS IN RANGE #####
#for i in range(0, 1024):
#    if isPrime(i):
#        print i, isPrime(i)
