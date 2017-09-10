class Call (object):
	def __init__(self, unique_id, caller_name, caller_number, time, reason):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone_number = caller_number
		self.time_of_call = time
		self.reason_for_call = reason
	def display(self):
		print "Unique ID: {}\nCaller Name: {}\nCaller Phone Number: {}\nTime Of Call: {}\nReason For Call: {}\n".format(self.unique_id, self.caller_name, self.caller_phone_number, self.time_of_call, self.reason_for_call)
		return self
class CallCenter (object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0
	def add (self, newCaller):
		self.calls.append(newCaller)
		self.queue_size += 1
		return self
	def remove (self):
		self.calls.pop(0)
		self.queue_size -= 1
		return self
	def info (self):
		for x in range(0,len(self.calls)):
			print "Name: {}\nPhone Number: {}\n".format(self.calls[x].caller_name, self.calls[x].caller_phone_number)
			return self
	

call1 = Call(111, "myron", "555-5555", "4:00pm", "aslkdjaslkd").display()
call2 = Call(112, "christina", "555-5553", "5:00pm", "puppies").display()

building = CallCenter()
building.add(call1).info()


