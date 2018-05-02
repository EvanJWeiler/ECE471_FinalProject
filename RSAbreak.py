import math
import time
import random
import multiprocessing as mp
import primefac
import gmpy2
from gmpy2 import mpz
processors = mp.cpu_count()

def genPQ(bits):
    p = generatePrime(2**(bits)-10000, 2**(bits))
    q = generatePrime(2**(bits)-10000, 2**(bits))
    return [p,q]

def genE(nPhi):
    #primes = primefac.primes(nPhi)
    #n = random.choice(primes)
    return 65537

def parallelF(arg):
    i = arg
    if isPrime(i):
        return i

def generatePrime(low, high):
    #primes = [i for i in range(low, high) if isPrime(i)]
    worker_pool = mp.Pool(processors)
    primes = [x for x in worker_pool.map(parallelF, range(low, high)) if x is not None]
    n = random.choice(primes)
    return n

def encrypt(m, key):
    return int(gmpy2.powmod(m, key[0], key[1]))
    #return m**key[0] % key[1]

def findNums(pubKey):
    n = pubKey[1]
    #for i in range(3,int(math.floor(n/3)+1)):
        #print i, n
    #    for j in range(3, int(math.floor(n/3)+1)):
    #        if i * j == n and isPrime(i) and isPrime(j):
    #            return [i, j]
    nums = list(primefac.primefac(n))
    nums[0] = int(nums[0])
    nums[1] = int(nums[1])
    return nums

def genPrivKey(nums, pubKey):
    e = pubKey[0]
    nPhi = (nums[0] - 1) * (nums[1] - 1)
    d = multInverse(e, nPhi)
    return [d, pubKey[1]]

def isPrime(num):
    return gmpy2.is_prime(num)
    #if num < 2: return False
    #for i in range(2, int(math.sqrt(num)+1)):
    #    if num % i == 0:
    #        return False
    #return True

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

print 'Welcome to RSA Breaker!'
time.sleep(.5)
print 'We support keys as large as XX bits!'
time.sleep(1)
bits = int(raw_input("Please enter the number of bits for the two large numbers (between 4-X): ")) # must be between 4 and X
[p,q] = genPQ(bits)
print("The two random primes are p = {} and q = {}").format(p, q)
time.sleep(1)
n = p * q
nPhi = (p-1)*(q-1)
e = genE(nPhi)
pubKey = [e, n]
print("The public key is: {}").format(pubKey)
time.sleep(1)
m = 1976
print "message:" , m
c = encrypt(m, pubKey)
time.sleep(1)
print "cypher:" , c
time.sleep(1)
print "RSA Breaker will now break the encrypted text"
startTime = time.time()
nums = findNums(pubKey)
print("RSA breaker found p and q to be: {}").format(nums)
privKey = genPrivKey(nums, pubKey)
print ("RSA breaker found the priv key to be: {}").format(privKey)
mNew = encrypt(c, privKey)
print "decrypted message:" , mNew
elapsedTime = time.time() - startTime
time.sleep(1)
print "decrypted message in: ", elapsedTime, " seconds"
