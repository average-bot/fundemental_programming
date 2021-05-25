playerPath = ''
winPath = 'ssdws'
trapPath = 'asas'
boostPath = 'waas'


print('You have been placed in a pitch-black labyrinth, without knowing if there is a way out or not.'\
      'Maybe there are traps? The only option available is to walk in a random direction and hope for the best,'\
      'hope that you do not walk into a wall, or even worse, that you walk in circles. But hurry up, you only have so many moves…\n')

print ('To move around use:\nw = up\na = left\ns = down\nd = right')

stepsLeft = 5
for i in range (stepsLeft):
    print(stepsLeft)
    playerPath += input('Enter direction: ')
    print(stepsLeft)
    if playerPath[i] == winPath[i]: # On the winpath
        print('ON the winpath')        
        if len(playerPath) == len(winPath):
            print('You survived! Well done adventurer!')
            break

    elif playerPath[i] == trapPath[i]: # On the trappath
        print('On the trappath')
        if len(playerPath) == len(trapPath):
            print('Oh no, a trap!')   
            # Delete last letter
            break

    elif playerPath[i] == boostPath[i]: # On the boostpath
        if len(playerPath) == len(boostPath):
            stepsLeft += 15
            print('A chocolate bar, I feel stronger')

    else: # If the player path doesnt match with any of the other paths
        print('Ouch! I can not walk though walls...')
        break
    stepsLeft -= 1

