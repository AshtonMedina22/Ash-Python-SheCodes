temperature = int(input("What is the temperature? "))
raining = input("Is it raining? (yes/no) ").lower()

if temperature >= 20 and raining == "yes":
    print("Don't forget your umbrella")
elif temperature >= 20 and raining == "no":
    print("Enjoy a sunny day")
elif temperature < 20 and raining == "yes":
    print("Don't forget your umbrella and your jacket")
else:
    print("Don't forget your jacket")
