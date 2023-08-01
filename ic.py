favorite_food = input("favorite_food: ")
age = input("age: ")
name = input("name: ")
last_name = input("last_name: ")
job = input("job: ")

try:
    age = int(age)
except ValueError:
    print("Invalid age input, please enter a valid integer.")
    exit()

introduce = """Hello, I'm {last_name}, but my friends call me {name}. I'm {age} years old, 
and my job is {job}. My favorite food is {favorite_food}, and I have {friend_count} friend.
"""
print(introduce.format(last_name=last_name, name=name, age=age, job=job, favorite_food=favorite_food, friend_count=friend_count))
print("Done✔")
