city = input("Enter the name of a city: ")
temperature = input("What is the temperature in " + city + "? ")

if not city or not temperature:
    print("Please try again and enter a city and temperature")
else:
    temperature = int(temperature)
    if temperature > 20:
        print(f"it is currently warm in {city} with a temperature of {temperature} degrees")
    elif temperature < 10:
        print(f"it is currently cold in {city} with a temperature of {temperature} degrees")
    else:
        print(f"it is currently chilly in {city} with a temperature of {temperature} degrees")
