import sys
import math
import time
import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


def generatePrime(low, high):
    primes = [i for i in range(low, high) if isPrime(i)]
    n = random.choice(primes)

    return n

def main():
    cls()
    
    startTime = time.time()

    print("Generating public values g and n...")

    g = 10 # generatePrime(2, 20)
    n = 2147483646 # generatePrime(1001, 2147470)

    print("\nWe will now demonstrate how the Diffie-Hellman key exchange works")
    time.sleep(2)
    print("We will simulate two users, Alice and Bob who the user will control")
    time.sleep(2)
    print("The two public values will be g = {} and n = {}\n").format(g, n)
    time.sleep(2)

    # GETTING PUBLIC KEYS
    
    timeBeforeInput = time.time() - startTime
    wait = True

    alicePrivate = raw_input("Please select the private key for Alice (between 1 and n): ") # must be between 1 and n
    while wait:
        if alicePrivate.isdigit():
            try:
                alicePrivate = int(alicePrivate)
            except ValueError:
                pass

        if isinstance(alicePrivate, int) and alicePrivate < n:
            wait = False
        elif isinstance(alicePrivate, int) and alicePrivate >= n:
            alicePrivate = raw_input("Alice's private key must be less than the public value n, please try again: ")
        else:
            alicePrivate = raw_input("That is not a valid value (integer), please try again: ")

    wait = True

    bobPrivate = raw_input("Please select the private key for Bob (between 1 and n): ") # must be between 1 and n
    while wait:
        if bobPrivate.isdigit():
            try:
                bobPrivate = int(bobPrivate)
            except ValueError:
                pass

        if isinstance(bobPrivate, int) and bobPrivate < n:
            wait = False
        elif isinstance(bobPrivate, int) and bobPrivate >= n:
            bobPrivate = raw_input("Bob's private key must be less than the public value n, please try again: ")
        else:
            bobPrivate = raw_input("That is not a valid value (integer), please try again: ")

    timeAfterInput = time.time()

    print("\nAlice's private key is {} and Bob's private key is {}.").format(alicePrivate, bobPrivate)
    time.sleep(2)
    print("Alice and Bob will now both perform g^key(mod n)")
    time.sleep(2)
    print("i.e. Alice and Bob will raise g to the power of their key, all mod n")
    time.sleep(3)

    aliceFirstMod = (g ** alicePrivate) % n
    bobFirstMod = (g ** bobPrivate) % n

    print("\nThe value that Alice obtains is {}").format(int(aliceFirstMod))
    time.sleep(2)
    print("The value that Bob obtains is {}").format(int(bobFirstMod))
    time.sleep(2)

    print("\nAlice will now send her value to Bob, and Bob will send his number to Alice")
    time.sleep(2)
    print("Alice and Bob will then raise the values they receive to their private key, all mod n")
    time.sleep(3)

    #import pdb; pdb.set_trace()

    aliceSecondMod = (bobFirstMod ** alicePrivate) % n
    bobSecondMod = (aliceFirstMod ** bobPrivate) % n

    print("\nThe value that Alice has now obtained is {}").format(aliceSecondMod)
    time.sleep(2)
    print("The value that Bob has now obtained is {}").format(bobSecondMod)
    time.sleep(3)

    print("\nAs you can see, the numbers that both Alice and Bob received are the same.")
    time.sleep(2)
    print("Their private keys were never transmitted over any medium, and they both have the same key.")
    time.sleep(2)
    print("This is the power of Diffie-Hellman")
    time.sleep(2)

    totalTime = (time.time() - timeAfterInput) + timeBeforeInput

    print("\nRuntime: {} seconds").format(totalTime - 33)


main()
