class mathDojo (object):
	def __init__(self):
		self.number = 0
		self.temp = 0
		self.listTemp = 0
	def add (self, num, *args):
		for x in range(0, len(args)):
			self.temp += args[x]
		self.number += num
		self.number += self.temp
		self.temp = 0
		return self
	def subtract (self, num, *args):
		for y in range(0,len(args)):
			self.temp += args[y]
		self.number -= num
		self.number -= self.temp
		self.temp = 0
		return self
	def result(self):
		print self.number
		return self

md = mathDojo().add(2).add(2, 5).subtract(3, 2).result()

