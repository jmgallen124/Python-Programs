# Program to demonstrate lists

# Declare list
list = ["Gallen", "Jeremy", 38]

# Print type
print(type(list))

# Print list
print(list)

# Print individual list elements
print(list[0])
print(list[1])
print(list[2])

# Change list elements
list[0] = "Jeremy"
list[1] = "Gallen"

# Display changed list and individual elements
print(list)
print(list[0])
print(list[1])

# Display element range
print(list[0:2])

# Append and display list
list.append("United States")
print(list)

# Pop and display list
list.pop()
print(list)

# Insert element into list and display
list.insert(1, "Michael")
print(list)

# Reverse and display list
list.reverse()
print(list)

# Edit, print, sort, and redisplay
list[1] = 24
list[2] = 42
list[3] = 55
print(list)
list.sort()
print(list)

# Add and display, multiply and display
print(list+list)
print(list*3)