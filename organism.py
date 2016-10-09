import random

class Organism:
	
	def __init__(self, name, generation):
		self.name = name
		self.energy = 1
		self.size = 1
		self.gen = generation
		
	def data(self):
		return self.name + " Gen " + str(self.gen) + "\n\tEnergy: " + str(self.energy) + "\n\tSize: " + str(self.size)


class Plant(Organism):		
	
	def live(self, organisms):
		self.eat()
		self.grow()
		self.reproduce(organisms)
		# Check for death
		if self.energy <= 0:
			organisms.remove(self)
			self = None
		elif self.size <= 0:
			organisms.remove(self)
			self = None
	
	def eat(self):
		self.energy += 1
	
	def grow(self):
		if self.energy >= 0.5:
			self.energy -= 0.5
			self.size += 0.5
	
	def reproduce(self, organisms):
		if self.energy >= 5:
			child = Plant(self.name, self.gen + 1)
			organisms.append(child)
			self.energy -= 4
			

class Herbivore(Organism):
	
	def live(self, organisms):
		self.eat(organisms)
		self.grow()
		self.reproduce(organisms)
		# Check for death
		if self.energy <= 0:
			organisms.remove(self)
			self = None
		elif self.size <= 0:
			organisms.remove(self)
			self = None
	
	def eat(self, organisms):
		prey = self.findprey(organisms)
		if prey != None:
			prey.size -= 1
			self.energy += 1
	
	def findprey(self, organisms):
		target = random.choice(organisms)
		if type(target) is Plant:
			return target
		else:
			return None
		
	def grow(self):
		if self.energy > 0.5:
			self.energy -= 0.5
			self.size += 0.5
			
	def reproduce(self, organisms):
		if self.energy < 4: # If it has enough energy to mate
			return
		mate = self.findmate(organisms)
		if mate != None:
			self.energy -= 3
			mate.energy -= 3
			child = Herbivore(self.name, self.gen + 1)
			organisms.append(child)
		
	def findmate(self, organisms):
		for organism in organisms: # Find a mate
			if type(organism) is Herbivore: # If it's an herbivore
				if organism.energy >= 4: # If it has enough energy to mate
					if organism != self: # It's not itself
						return organism
		return None
