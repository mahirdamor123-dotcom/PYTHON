print("welcome to the personal data collector")

name=input('enter your name')
age=int(input('enter your age'))
height=  float(input('enter your height (cm): '))
fav_num=int(input(' enter your favourite number: '))

birth_year= 2026-age

height_int = int(height)

print("\n--- Variable Details ---")

print(f"name: {name}")
print(f"type: {type(name)}")
print(f"memory Address: {id(name)}")

print(f"age: {age}")
print(f"type: {type(age)}")
print(f"memory Address: {id(age)}")

print(f"height: {height}")
print(f"type: {type(height)}")
print(f"Memory Address: {id(height)}")

print(f"fav_num: {fav_num}")
print(f"type: {type(fav_num)}")
print(f"memory Address: {id(fav_num)}")

print("\n---- Summary ----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} m")
print(f"Favourite number: {fav_num}")
print(f"Approximate Birth Year: {birth_year}")

print("\nThank you for using the program")