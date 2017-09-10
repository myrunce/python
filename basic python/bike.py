#Part 1
class Bike (object):
	def __init__(self, price, speed):
		self.price = price
		self.max_speed = speed
		self.miles = 0
	#part 2. All of part 2 can return self
	def displayInfo(self):
		print "Price: {}, Max speed: {}, Total miles: {}".format(self.price, self.max_speed, self.miles)
		return self 
	def ride(self): 
		self.miles += 10
		return self
	def reverse(self):
		if self.miles >= 5: #to prevent the miles to go negative
			self.miles -= 5
		return self
		

roadster = Bike ("$75.00", "30mph")
mountain = Bike ("$90.00", "25mph")
fixie = Bike ("$100.00", "40mph")

roadster.ride().ride().ride().reverse().displayInfo()
mountain.ride().ride().reverse().reverse().displayInfo()
fixie.reverse().reverse().reverse().displayInfo()
