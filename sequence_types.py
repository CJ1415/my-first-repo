list = [400, "Hello", 100, 1+5, 5.5]
len(list)
list.append(500)
index = 0
list.insert(index, 11)
list.remove(500)
len(list)
list[1] = 100
print(list)
print(type(list))
tuple0 = tuple(list)
print(type(tuple0))
print(len(tuple0))
# tuple0[0] = 100

car_details = {"car_make": "Toyota", "car_model": "Corolla"}
print(car_details)
make = car_details["car_make"]
print(car_details)
car_details["year"] = 2024
print(car_details)
car_details["colour"] = "Red"
print(car_details)
