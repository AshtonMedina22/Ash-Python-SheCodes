def get_city_temperature():
    city = input("What city are you in? ")
    temperature = input(f"What is the current temperature in {city}? ")
    
    if city and temperature:
        print(f"You are in {city} and it is currently {temperature}ºC")
    else:
        print("You did not provide a city and/or temperature.")

get_city_temperature()
get_city_temperature()
