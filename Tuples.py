# Program to demonstrate tuples

# Declare tuples
tup1 = ("Gallen", "Jeremy", 38, "Texas")
tup2 = ("Coryell", "Copperas Cove")
tup3 = (17, 5, 8, 10, 1)

# Display type
print(type(tup1))

# Print tuple
print(tup1)

# Print individual tuple elements
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
print(tup1[-1])
print(tup1[-2])
print(tup1[-3])
print(tup1[-4])

# Print tuple ranges
print(tup1[0:1])
print(tup1[2:3])

# Display tuple sizes
print(len(tup1))
print(len(tup2))

# Add tuples
print(tup1 + tup2)
print(tup2 + tup1)

# Repeat tuple elements
print(tup1*3 + tup2*2)
print(tup2*4 + tup2*3)

# Print minimum and maximum values of tuples
print(min(tup3))
print(max(tup4))