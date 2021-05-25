# The truck's volume
truck_volume = 0

# The volume of each bag
big_volume = 80
medium_volume = 50
small_volume = 20

# The amount of bags
big_amount = 0
medium_amount = 0
small_amount = 0

# The value of each bag
big_value = 60000
medium_value = 30000
small_value = 10000

# The total value of all the bags in SEK
total_value = 0

# Prints the welcome text on the screen
print('Welcome to the Money Bag Transport Calculator (M.B.T.C)')
print('-------------------------------------------------------\n')

# Asking the user to write in the volume of the truck
# until the user enters a value that's larger than 100.
while truck_volume < 100:
    truck_volume = int(input('What is the volume of the truck (>= 100L): '))

# Truck volume becomes the free space
free_space = truck_volume

# When free space is larger or the same as the big bag's volume
# One big bag volume will be subtracted from the free space
# Then we will count another big bag
while free_space >= big_volume:
    free_space = free_space - big_volume
    big_amount += 1

# -II- but with medium bag's values
while free_space >= medium_volume:
    free_space = free_space - medium_volume
    medium_amount += 1

# -II- but with small bag's values
while free_space >= small_volume:
    free_space = free_space - small_volume
    small_amount += 1

# Prints the amount of each bag on the screen
print('\nPacking plan')
print('------------')
print(big_amount, 'big bags')
print(medium_amount, 'medium bags')
print(small_amount, 'small bags')

# Calculates the total value of the bags in SEK
total_value = (big_amount*big_value) + (medium_amount*medium_value)\
     + (small_amount*small_value)
# Prints the volume of free space and the total value of the begs on the screen
print('\nSpace left : ', str(free_space)+'L',
      '\nTotal value:', str(total_value)+'kr')
