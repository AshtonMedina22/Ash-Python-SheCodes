# Create a dictionary of 3 countries you'd like to visit as a key and their capital city a value
countries = {
    "Austria": "Vienna",
    "Japan": "Tokyo",
    "Ecuador": "Quito"
}

# Print out the dictionary
print(countries)

# Remove your least favorite country from the dictionary
countries.pop("Austria")

# Print out the dictionary
print(countries)

# Add another country you'd like to visit
countries["Colombia"] = "Bogota"

# Print out the dictionary
print(countries)

# Display the capital of each country (one at a time, don't use a loop)
print("The capital city of Colombia is " + countries["Colombia"])
print("The capital city of Japan is " + countries["Japan"])
print("The capital city of Ecuador is " + countries["Ecuador"])
