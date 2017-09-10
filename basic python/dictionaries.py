me = {"name":"Myron", "age":"25", "country of birth":"United States", "favorite language":"Python"}
def aboutMe (var):
	temp = var.items()
	print "My {} is {}".format(temp[2][0], temp[2][1])
	print "My {} is {}".format(temp[0][0], temp[0][1])
	print "My {} is The {}".format(temp[3][0], temp[3][1])
	print "My {} is {}".format(temp[1][0], temp[1][1])

aboutMe(me)
