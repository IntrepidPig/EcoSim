#!/usr/bin/python

import time

from organism import *

runningsim = True

organisms = []

def loop():
	i = 0
	for organism in organisms:
		organism.live(organisms)
		print(organism.data())
		i += 1
	print()

testplant = Plant("Test Plant", 1)
testplant2 = Plant("Test Plant", 1)
testherbivore = Herbivore("Test Herbivore", 1)
testherbivore2 = Herbivore("Test Herbivore", 1)
organisms.append(testplant)
organisms.append(testplant2)
organisms.append(testherbivore)
organisms.append(testherbivore2)

while runningsim:
	loop()
	time.sleep(0.1)
