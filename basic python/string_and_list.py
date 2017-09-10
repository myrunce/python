#Find and Replace
words = "Its Thanksgiving day. It's my birthday too!"
print words
words.find('day')
words = words.replace("day", "month")
print words

#Min and Max
x = [2,54,-2,7,12,98]
print min(x), max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]
y = [x[0], x[len(x) - 1]]

#new List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[len(x)/2:]
second_list.insert(0, first_list)
print second_list
