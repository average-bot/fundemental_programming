xPlayer = 0
yPlayer = 0

step = 10

xTrap = 10
yTrap = -10

xBoost = 70
yBoost = 30

print('You have been placed in a pitch-black labyrinth, without knowing if there is a way out or not.'\
      'Maybe there are traps? The only option available is to walk in a random direction and hope for the best,'\
      'hope that you do not walk into a wall, or even worse, that you walk in circles. But hurry up, you only have so many moves…\n')

print ('To move around use:\nw = up\na = left\ns = down\nd = right')

while True:
    direction = input('Enter direction: ')

    if direction == 'w':
        yPlayer += step
    elif direction == 'a':
        xPlayer -= step
    elif direction == 's':
        yPlayer -= step
    elif direction == 'd':
        xPlayer += step

    if xPlayer and xTrap == yPlayer and yTrap:
        print('You got trapped')   
      


path = 'ADSWSSDAS'
trap = 'ASDWSWS'


print(xPlayer, yPlayer)
