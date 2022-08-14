# Program to demonstrate lambda functions

# Main function to get input
num_to_square = input("Please type in the number to square: ")
squared_num = lambda num_to_square: num_to_square * num_to_square
print(squared_num(int(num_to_square)))