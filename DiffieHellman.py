import sys
import math
import time
import os
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

	
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
	return True

	
def generatePrime(low, high):
	primes = [i for i in range(low, high) if isPrime(i)]
	n = random.choice(primes)
	
	return n

def main():
	cls()
	g = generatePrime(2, 131)
	n = generatePrime(1001, 214747)

	print("We will now demonstrate how the Diffie-Hellman key exchange works")
	time.sleep(1)
	print("We will simulate two users, Alice and Bob who the user will control")
	time.sleep(1)
	print("The two public values will be g = {} and n = {}").format(g, n)
	time.sleep(1)

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
