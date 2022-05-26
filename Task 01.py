class Vehicles:
	def __init__(self,*arg):
		self.no_of_wheels = arg[0]
		self.fuel_type = arg[1]

	def bike(self):
		print("\nNumber of wheels are ",self.no_of_wheels,"\nFuel type is ", self.fuel_type)
	
	def car(self):
		print("\nNumber of wheels are ",self.no_of_wheels,"\nFuel type is ", self.fuel_type)
	
	def truck(self):
		print("\nNumber of wheels are ",self.no_of_wheels,"\nFuel type is ", self.fuel_type)
	


print("1. Bike\n2. Car\n3. Truck")

choice = int(input("Enter choice: "))

fuel_type = input("Enter fuel type: ")
no_of_wheels = input("Enter no of wheels: ")

obj = Vehicles(no_of_wheels,fuel_type)

if (choice == 1):
	print("Vehicle is Bike")
	obj.bike()
elif (choice == 2):
	print("Vehicle is Car")
	obj.car()
elif (choice == 3):
	print("Vehicle is Truck")
	obj.truck()