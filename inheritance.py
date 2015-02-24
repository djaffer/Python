class Parent():
	def __init__(self,last_name,eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color



class Child(Parent):
	def __init__(self,last_name,eye_color,number_of_toys):
		Parent.__init__(self,last_name,eye_color)
		self.number_of_toys = number_of_toys

if __name__ == "__main__":
	billy_cyrus = Parent("Cyrus","blue")
	print(billy_cyrus.last_name)

	danish_jaffer = Child("Danish","Jaffer",4)
	print(danish_jaffer.last_name)
	print(danish_jaffer.number_of_toys)
