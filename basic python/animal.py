class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1 
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.health
		return self
		
class dog(animal):
	def __init__(self, name, health):
		super(dog, self).__init__(name, health)
		self.health = 150
	def pet (self):
		self.health += 5
		return self
		
class dragon(animal):
	def __init__(self, name, health):
		super(dragon, self).__init__(name, health)
		self.health = 170
	def fly (self):
		self.health -= 10
		return self
	def displayDhealth (self):
		self.displayHealth()
		print "I am a Dragon."
		
myron = animal("Myron", 120)
myron.walk().walk().walk().run().run().displayHealth()
Benji = dog("Benji", 50)
print Benji.name
Benji.walk().walk().walk().run().run().pet().displayHealth()
magic = dragon("puffy", 30)
magic.displayDhealth()
christina = animal("Christina", 120)
christina.displayHealth()


