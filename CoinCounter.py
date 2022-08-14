# Python program to divide coins

# Declare coin number variables
numCoins = 0
oneCoin = 0
twoCoin = 0
fiveCoin = 0
tenCoin = 0
twentyfiveCoin = 0
fiftyCoin = 0
hundredCoin = 0

# Get coin value from user
coinValue = int(input("Enter the coin value: "))

# Count hundred coins
hundredCoin = int(coinValue / 100)
numCoins += hundredCoin
coinValue %= 100

# Count fifty coins
fiftyCoin = int(coinValue / 50)
numCoins += fiftyCoin
coinValue %= 50

# Count twenty-five coins
twentyfiveCoin = int(coinValue / 25)
numCoins += twentyfiveCoin
coinValue %= 25

# Count ten coins
tenCoin = int(coinValue / 10)
numCoins += tenCoin
coinValue %= 10

# Count five coins
fiveCoin = int(coinValue / 5)
numCoins += fiveCoin
coinValue %= 5

# Count two coins
twoCoin = int(coinValue / 2)
numCoins += twoCoin
coinValue %= 2

# Count one coins
oneCoin += coinValue
numCoins += oneCoin

# Output coin values
print("\nCoin Values\n")

# Print one coins
print("One Coins: ",oneCoin)

# Print two coins
print("Two Coins: ",twoCoin)

# Print five coins
print("Five Coins: ",fiveCoin)

# Print ten coins
print("Ten Coins: ",tenCoin)

# Print twenty-five coins
print("Twenty-Five Coins: ",twentyfiveCoin)

# Print fifty coins
print("Fifty Coins: ",fiftyCoin)

# Print hundred coins
print("Hundred Coins: ",hundredCoin,"\n")

# Print total coins
print("Total Coins: ",numCoins)