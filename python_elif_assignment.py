temperature = input("What is the temperature? ")
temperature = int(temperature)

rainy = input("Is it raining? (yes/no) ")
rainy = rainy.lower()

if temperature > 20 and rainy == 'no':
    print("Enjoy a sunny day")
elif temperature > 20 and rainy == 'yes':
    print("Don't forget your umbrella")
elif temperature < 20 and rainy == 'yes':
    print("Don't forget your umbrella and your jacket")
else:
    print("Don't forget your jacket")
