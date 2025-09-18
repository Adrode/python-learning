name = input("What's your name?: ")
age = input("How old are you?: ")

print("Hello " + name + "!")
if int(age) >= 18:
    print("You're an adult")
elif int(age) < 18:
    print("You're a kid")
else:
    print("Something went wrong!")