# Program to demonstrate strings

# Declare strings
str1 = "Every man is entitled to his own opinions, but not his own facts."
str2 = '''Liars are never believed, forsooth,
Even when liars tell the truth.'''

# Print first string
print(str1)
print("\n")

# Print second string
print(str2)
print("\n")

# Print letters of first string with positive indexes
print(str1[0])
print(str1[4])
print(str1[2])
print("\n")

# Print letters of second string with positive indexes
print(str2[0])
print(str2[2])
print(str2[10])
print(str2[23])
print("\n")

# Print letters of first string with negative indexes
print(str1[-3])
print(str1[-10])
print(str1[-9])
print(str1[-8])
print("\n")

# Print letters of second string with negative indexes
print(str2[-2])
print(str2[-4])
print(str2[-3])
print("\n")

# Print index ranges of first string
print(str1[6:9])
print(str1[-6:-1])
print("\n")

# Print index ranges of second string
print(str2[0:5])
print(str2[-6:-1])
print("\n")

# Display lengths of strings
print(len(str1))
print(len(str2))
print("\n")

# Lowercase all letters of strings
print(str1.lower())
print(str2.lower())
print("\n")

# Uppercase all letters of strings
print(str1.upper())
print(str2.upper())
print("\n")

# Output ocurrences of certain words in strings
print(str1.count("own"))
print(str2.count("when"))
print("\n")

# Replace characters in strings and output
str1.replace("man","person", 1)
print(str1)
str2.replace("when","if", 1)
print(str2)
print("\n")

# Print indexes of substrings
print(str1.find("entitled"))
print(str2.find("forsooth"))
print("\n")

# Program to demonstrate strings

# Declare strings
str1 = "Every man is entitled to his own opinions, but not his own facts."
str2 = '''Liars are never believed, forsooth,
Even when liars tell the truth.'''

# Print first string
print(str1)
print("\n")

# Print second string
print(str2)
print("\n")

# Print letters of first string with positive indexes
print(str1[0])
print(str1[4])
print(str1[2])
print("\n")

# Print letters of second string with positive indexes
print(str2[0])
print(str2[2])
print(str2[10])
print(str2[23])
print("\n")

# Print letters of first string with negative indexes
print(str1[-3])
print(str1[-10])
print(str1[-9])
print(str1[-8])
print("\n")

# Print letters of second string with negative indexes
print(str2[-2])
print(str2[-4])
print(str2[-3])
print("\n")

# Print index ranges of first string
print(str1[6:9])
print(str1[-6:-1])
print("\n")

# Print index ranges of second string
print(str2[0:5])
print(str2[-6:-1])
print("\n")

# Display lengths of strings
print(len(str1))
print(len(str2))
print("\n")

# Lowercase all letters of strings
print(str1.lower())
print(str2.lower())
print("\n")

# Uppercase all letters of strings
print(str1.upper())
print(str2.upper())
print("\n")

# Output ocurrences of certain words in strings
print(str1.count("own"))
print(str2.count("when"))
print("\n")

# Replace characters in strings and output
print(str1.replace("man","person", 1))
print(str2.replace("when","if", 1))
print("\n")

# Print indexes of substrings
print(str1.find("entitled"))
print(str2.find("forsooth"))
print("\n")

# Demonstrate split function and output strings
print(str1.split(','))
print(str2.split(','))
print("\n")