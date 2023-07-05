from classe.car import * 

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#my_new_car.odometer_reading = 23
my_new_car.update_odometer(100)
my_new_car.read_odometer()


my_new_car2 = Car('subaru','outback',2013)
print(my_new_car2.get_descriptive_name())

my_new_car2.update_odometer(23500)
my_new_car2.increment_odomoter(100)
my_new_car2.read_odometer()

