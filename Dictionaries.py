# Program to demonstrate dictionaries in Python

# Canadian House of Commons
CanadaHoC = {"Liberals": 158, "Conservatives": 119, "Bloc Québécois": 32, "New Democrats": 25, "Greens": 2}

# Array with leftist parties
CanadaLeft = {"Liberals": 0, "New Democrats": 0, "Greens": 0}

# Print dictionary
print(CanadaHoC)

# Print type
print(type(CanadaHoC))

# Print keys
print(CanadaHoC.keys())

# Print values
print(CanadaHoC.values())

# Print items
print(CanadaHoC.items())

# Add item and print updated dictionary
CanadaHoC["Republicans"] = 0
print(CanadaHoC)

# Change existing item, display, and change back
CanadaHoC["Conservatives"] = 120
print(CanadaHoC)
CanadaHoC["Conservatives"] = 119

# Update dictionary and print
CanadaLeft.update(CanadaHoC)
print(CanadaLeft)

# Pop value and display dictionary again
CanadaHoC.pop("Republicans")
print(CanadaHoC)