age = int(input("age : "))
name = str(input("name : "))
last_name = str(input("last_name"))
job = str(input("job : "))
interduce = (
    "hello im {0} but my friends call me {1} im {2} years old and my job is {3}")
print(interduce.format(last_name, name, age, job))
print("Done✔")