class patient (object):
	def __init__(self, ident, name, allergies):
		self.identity = ident
		self.name = name 
		self.allergies = allergies
		self.bed_number = "none"

class hospital (object): 
	def __init__(self, name, capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
	def admit (self, patient):
		if len(self.patients) < self.capacity:
			self.patients.append(patient)
			patient.bed_number = len(self.patients) 
			print "Admission complete."
		else:
			print "Hospital is currently full."
		return self
	def discharge (self, patient):
		for x in range(0, len(self.patients)):
			if patient == self.patients[x]:
				self.patients[x].bed_number = "none"
				self.patients.pop(x)
		return self
		
patient1 = patient(1, "myron", "none")
patient2 = patient(2, "christina", "none")
building = hospital("st.rose", 1)
building.admit(patient1)
print patient1.bed_number
building.admit(patient2)
building.discharge(patient1)
print patient1.bed_number
		
