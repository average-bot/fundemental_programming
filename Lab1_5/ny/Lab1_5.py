# The player's path, which will be changed according to the input of the user
playerPath = ''
# The path from the startpoint to the endpoint
winPath = 'wwwwddddsssssdddwwwwawww'
# The paths from the startpoint to the traps and boosts
trapPath1 = 'wwwwwwaassssssssddd'
trapPath2 = 'wwwwdddwwd'
trapPath3 = 'wwwwddddsssssdddwwwwawwd'
boostPath1 = 'wwwwdddwwa'
boostPath2 = 'wwwwddddsssssdddwwa'

# Game's description
print('You have been placed in a pitch-black labyrinth,'
      'without knowing if there is a way out or not.'
      'Maybe there are traps? The only option available'
      'is to walk in a random direction and hope for the best,'
      'hope that you do not walk into a wall, or even worse,'
      'that you walk in circles. But hurry up, you only have so many moves…\n')

# Instructions for the user
print('To move around use:\nw = up\na = left\ns = down\nd = right')

# The game will start with a specific amount of steps,
# which in this case is 20.
stepsLeft = 20
# Before the start of the game the player will have stepped 0 steps,
# which will later be changed.
stepped = 0
# A counter for how many times the player has hit the wall.
wallbang = 0

# A condition-controlled loop that will loop
# as many times there are steps left.
while stepsLeft > 0:
    # Starting with a validation loop so that there wont be any GIGO
    # The user can only continue if they input an w, a, s or d.
    direction = ''
    while direction != 'a' and direction != 's' \
            and direction != 'w' and direction != 'd':
        direction = input('Enter direction: ')

    # The user's input will be added to the player path,
    # so it can be compared to the other paths later on.
    playerPath += direction
    # Every time a player makes a step it will be counted
    stepped += 1
    # And every time a player makes a step,
    # the number of steps left will decrease by 2
    stepsLeft -= 1

    # If there aren't any steps left the game will be over.
    if stepsLeft == 0:
        print('Game over! You did not reach the exit in time.')
        break

    # If the player has the same path as the win path the user has won
    elif playerPath[0:stepped] == winPath[0:stepped]:
        if len(playerPath) == len(winPath):
            print('You survived! Well done adventurer!')
            break

    # If the player has the same path as the trap path,
    # the player will start their journey from the beginning
    elif playerPath[0:stepped] == trapPath1[0:stepped]:
        if len(playerPath) == len(trapPath1):
            print('oh no, a trap!')
            playerPath = ''
            stepped = 0
    # -II-
    elif playerPath[0:stepped] == trapPath2[0:stepped]:
        if len(playerPath) == len(trapPath2):
            print('oh no, a trap!')
            playerPath = ''
            stepped = 0
    # -II-
    elif playerPath[0:stepped] == trapPath3[0:stepped]:
        if len(playerPath) == len(trapPath3):
            print('oh no, a trap!')
            playerPath = ''
            stepped = 0

    # If the player has the same path as the boost path,
    # the player will continue their journey with 15 extra
    # steps and new paths for the objectives.
    elif playerPath[0:stepped] == boostPath1[0:stepped]:
        if len(playerPath) == len(boostPath1):
            print('A chocolate bar, I feel stronger')
            stepsLeft += 15
            stepped = 0
            playerPath = ''
            winPath = 'dssdsssssdddwwwwawww'
            trapPath1 = 'dssaaawwaassssssssddd'
            trapPath2 = 'dd'
            trapPath3 = 'dssdsssssdddwwwwawwd'
            boostPath2 = 'dssdsssssdddwwa'

    # -II-
    elif playerPath[0:stepped] == boostPath2[0:stepped]:
        if len(playerPath) == len(boostPath2):
            print('A chocolate bar, I feel stronger')
            stepsLeft += 15
            stepped = 0
            playerPath = ''
            winPath = 'dwwawww'
            trapPath1 = 'dssaaawwwwwaaaawwaassssssssddd'
            trapPath2 = 'dssaaawwwwwawwd'
            trapPath3 = 'dwwawwd'
            boostPath1 = 'dssaaawwwwwawwa'

    # If the player path doesnt match with any of the other paths,
    # they hit one of the walls
    else:
        print('Ouch! I can not walk though walls...')
        # The last letter will be removed from the path
        # and a step will be taken back
        playerPath = playerPath[:-1]
        stepped -= 1
        # If the player wants to walk outside the table.
        wallbang += 1
        if wallbang >= 5:
            print('oh no, a trap!')
