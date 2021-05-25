playerPath = ''
winPath = 'wdwddwdwawwddwd'
trapPath = 'wdwdwawawwd'
boostPath = 'ddddwdwdwddwd'

print('You have been placed in a pitch-black labyrinth, without knowing if there is a way out or not.'\
      'Maybe there are traps? The only option available is to walk in a random direction and hope for the best,'\
      'hope that you do not walk into a wall, or even worse, that you walk in circles. But hurry up, you only have so many moves…\n')

print ('To move around use:\nw = up\na = left\ns = down\nd = right')

stepsLeft = 20
stepped = 0

while stepsLeft > 0:

    direction =''
    while direction != 'a' and direction != 's' and direction != 'w' and direction != 'd':
        direction = input('Enter direction: ')

    playerPath += direction
    stepped += 1
    stepsLeft -= 1

    if playerPath[0:stepped] == winPath[0:stepped]:
        if len(playerPath) == len(winPath):
            print('You survived! Well done adventurer!')
            break

    elif playerPath[0:stepped] == trapPath[0:stepped]:
        if len(playerPath) == len(trapPath):
            print('oh no, a trap!')
            playerPath = ''
            stepped = 0
            
    elif playerPath[0:stepped] == boostPath[0:stepped]:
        if len(playerPath) == len(boostPath):
            print('A chocolate bar, I feel stronger')
            stepsLeft += 15
            stepped = 0
            playerPath = ''
            winPath = 'waasawasaawwddwd'
            trapPath = 'asaasasasaaaawdwdwawawwd'
            boostPath = ''

    elif stepsLeft == 0:
        print('Game over! You did not reach the exit in time.')
        break

    else: # If the player path doesnt match with any of the other paths
        print('Ouch! I can not walk though walls...')
        # Delete last letter
        playerPath = playerPath[:-1]
        stepped -= 1