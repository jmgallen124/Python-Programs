# Program to demonstrate sets in Python

# Declare sets
set1 = {"Gallen", "Jeremy", "Michael", "Tannery", "Michael"}
set2 = {"Jeremy", "Michael", "Mary"}

# Display type and output
print(type(set1))
print(set1)

# Add items and display again
set1.add("Rosemary")
set1.add("Tannery")
print(set1)

# Remove element and display again
set1.remove("Rosemary")
print(set1)

# Update and display
set1.update(["Harrison", "Edgar", "Ray"])
print(set1)

# Display union of sets
print(set1.union(set2))

# Display intersection of sets
print(set1.intersection(set2))