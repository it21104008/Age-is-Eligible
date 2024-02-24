age = int(input("What is ur Age:"))

while age < 18 or age > 21:
    print("You are not eligible")
    age = input("What is ur Age:")

print(f"Your age is {age}...You are Eligible")
