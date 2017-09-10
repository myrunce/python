class product (object):
	def __init__(self, price, itemName, weight, brand, cost):
		self.price = price
		self.item_name = itemName
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self
	def add_tax(self, tax):
		self.tax = tax
		return self
	def returnItem (self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		elif reason == "in box, like new":
			self.status = "for sale"
		elif reason == "open box":
			discount = self.price * .20
			self.price -= discount
			self.status = "Used"
		return self
	def displayInfo(self):
		print "Price: {}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}\n".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)
		return self
	
item1 = product(45, "gum", "1 lb", "gummy", 1.00)
item2 = product(25, "cheese", "3 lb", "cheesy", 5.00)
item3 = product(15, "mints", "0.14 lb", "minty", .90)

item1.sell().displayInfo().returnItem("defective").displayInfo()
			
			
		
