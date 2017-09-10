def draw_stars (arr):
	for x in arr:
		if isinstance (x, int):
			star_arr = []
			for i in range(0,x):
				star_arr.append("*")
			print ''.join(star_arr)
		elif isinstance (x, str):
			letter_arr = []
			first_letter = x[0][0]
			conversion = len(x)
			for z in range(0,conversion):
				letter_arr.append(first_letter)
			temp = "".join(letter_arr)
			print temp.lower()
							
x = [1,"Myron",3,4,"Christina"]
draw_stars(x)
			
