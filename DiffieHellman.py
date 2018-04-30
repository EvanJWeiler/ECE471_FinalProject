import sys
import math
import time
import os

g = 5
n = 4581 # generateLargePrime()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cls()

    print("We will now demonstrate how the Diffie-Hellman key exchange works")
    time.sleep(2)
    print("We will simulate two users, Alice and Bob who the user will control")
    time.sleep(2)
    print("The two public values will be g = {} and n = {}").format(g, n)
    time.sleep(2)

    # GETTING PUBLIC KEYS

    wait = True

    alicePrivate = raw_input("Please select the private key for Alice: ") # must be between 1 and n
    while wait:
        if alicePrivate.isdigit():
            try:
                alicePrivate = int(alicePrivate)
            except ValueError:
                pass

        if isinstance(alicePrivate, int) and alicePrivate < n:
            wait = False
        elif isinstance(alicePrivate, int) and alicePrivate > n:
            alicePrivate = raw_input("Alice's private key must be less than the public value n, please try again: ")
        else:
            alicePrivate = raw_input("That is not a valid value (integer), please try again: ")

    wait = True

    bobPrivate = raw_input("Please select the private key for Bob: ") # must be between 1 and n
    while wait:
        if bobPrivate.isdigit():
            try:
                bobPrivate = int(bobPrivate)
            except ValueError:
                pass

        if isinstance(bobPrivate, int) and bobPrivate < n:
            wait = False
        elif isinstance(bobPrivate, int) and bobPrivate > n:
            bobPrivate = raw_input("Bob's private key must be less than the public value n, please try again: ")
        else:
            bobPrivate = raw_input("That is not a valid value (integer), please try again: ")



main()
