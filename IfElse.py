# Program to demonstrate if/else statements.

# Declare variables
a = 7
b = 13
c = 5
tup = (2, 4, 6, 8, 10)
lis = [3, 6, 9, 12, 15]
dict = {"Sons": 3, "Daughters": 1}

# If/else statement
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
elif a == b:
    print("a and be are equal")
else:
    print("something is wrong with the values")
    
# Find which number is greatest
if ((a > b) & (a > c)):
    print("a is the highest number")
elif ((b > a) & (b > c)):
    print("b is the highest number")
elif ((c > a) & (c > b)):
    print("c is the highest number")
else:
    print("something is wrong with the values")
    
# Demonstrate if/else with tuple
if 8 in tup:
    print("8 is in the tuple")
else:
    print("8 is not in the tuple")

# Demonsrate when value not present in tuple
if 7 in tup:
    print("7 is in the tuple")
else:
    print("7 is not in the tuple")

# Print list
print(lis)

# If/else with list
if lis[2] == 9:
    lis[2] *= 2
    print(lis)
else:
    print("value is not in list")

# If/else with dictionary
if dict["Sons"] == 3:
    print("There are 3 sons in the family.")
elif dict["Sons"] > 3:
    print("There are more than 3 sons in the family.")
elif dict["Sons"] < 3:
    print("There are less than 3 sons in the familiy.")
else:
    print("Something is wrong with the dictionary.")