cars = [
    {'name': 'Honda yazz', 'year': 2005},
    {'name': 'Hyundai i20', 'year': 2013},
    {'name': 'Fiat panda', 'year': 2003},
]

#def f(car):
#    return car["name"]

cars.sort(key=lambda car: car["name"])
print(cars)