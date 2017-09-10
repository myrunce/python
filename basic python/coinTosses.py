import random
def coinTosses(tosses):
	heads = 0
	tails = 0
	x = 1
	while x <= tosses:
		results = random.randint(0, 100)
		if results <= 50:
			tails += 1
			print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(x, heads, tails)
			x += 1
		elif results > 50:
			heads += 1
			print "Attempt #{}: Throwing a coin... It's a Head! ... Got {} head(s) so far and {} tail(s) so far".format(x, heads, tails)
			x += 1
	print "End of program, thank you!"

coinTosses()
	
