truck_volume = 0

big_volume = 80
medium_volume = 50
small_volume = 20

big_amount = 0
medium_amount = 0
small_amount = 0

big_value = 60000
medium_value = 30000
small_value = 10000

total_value = 0

print('Welcome to the Money Bag Transport Calculator (M.B.T.C)')
while truck_volume < 100:
    truck_volume = int(input('What is the colume of the truck (>= 100L):'))

free_space = truck_volume

while free_space >= big_volume:
    free_space = free_space - big_volume
    big_amount += 1

print('1. How many big bags (', big_volume,'L) can we fit in ', truck_volume ,'L? Answer is ', big_amount,'.', '\nWe now have ', free_space,'L left in truck.')


while free_space >= medium_volume:
    free_space = free_space - medium_volume
    medium_amount += 1

print('2. How many medium bags (', medium_volume,'L) can we fit in ', truck_volume - (big_volume*big_amount),'L? Answer is ', medium_amount,'.', '\nWe now have ', free_space,'L left in truck.')


while free_space >= small_volume:
    free_space = free_space - small_volume
    small_amount += 1

print('3. How many medium bags (', small_volume,'L) can we fit in ', truck_volume - (big_amount*big_volume) - (medium_amount*medium_volume),'L? Answer is ', small_amount,'.', '\nWe now have ', free_space,'L left in truck.')

total_value = (big_amount*big_value) + (medium_amount*medium_value) + (small_amount*small_value)
print('Space left  : ', free_space, 'L', '\nTotal value: ', total_value,'kr')