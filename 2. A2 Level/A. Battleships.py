# Battleships
# Author: Kelvin Zhang
# Date Created: 2016-09-11

NUMBER_OF_SHIPS = 5
X_LENGTH = 8
Y_LENGTH = 8

# Create 8x8 array of battleships
battleships = [
    [True, True, True, False, True, False, False, False],
    [False, False, False, False, True, False, False, False],
    [False, False, False, False, True, False, True, False],
    [False, False, False, False, True, False, False, False],
    [True, False, False, False, True, False, False, False],
    [True, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, True, True],
    [True, False, False, False, False, False, False, False]
]

# Create 8x8 array of shots made
shots = [[False for j in range(X_LENGTH)] for i in range(Y_LENGTH)]
shotCount = 0
shipsSunk = 0

while True:
    # Enter coordinates
    xInput = input("Enter the x-coordinate [1-{!s}]:".format(X_LENGTH))
    if not xInput.isdigit():
        print("Your x-coordinate must be a digit. Try again.")
        continue
    x = int(xInput)
    if x < 1 or x > X_LENGTH:
        print("Your x-coordinate must be between 1 and {!s}. Try again.".format(X_LENGTH))
        continue

    yInput = input("Enter the y-coordinate [1-{!s}]:".format(Y_LENGTH))
    if not yInput.isdigit():
        print("Your y-coordinate must be a digit. Try again.")
        continue
    y = int(yInput)
    if y < 1 or y > Y_LENGTH:
        print("Your x-coordinate must be between 0 and {!s}. Try again.".format(Y_LENGTH))
        continue

    # Humans view co-ordinates (1-8) from the bottom-left corner, whereas programmers look at arrays from the top-right corner (0-7)
    # As a result, the points are converted into programmer-friendly form
    x -= 1
    y = Y_LENGTH - y

    # Check whether the coordinates have been entered before, and shoot if not
    if shots[y][x] is True:
        print("You have already taken a shot at these coordinates. Enter a different set of coordinates.")
        continue
    shots[y][x] = True
    shotCount += 1

    # Check whether a ship exists at this location
    if battleships[y][x] is True:
        print("The missile hits a target...")

        # Check whether there whether the ship extends horizontally or vertically
        # If so, then it must be checked whether the ship is destroyed
        # If not, then the ship is a one-length ship, which is destroyed
        isShipDestroyed = False
        shipLength = 1
        shipHits = 1

        if (x > 0 and battleships[y][x - 1] is True) or (x < 8 and battleships[y][x + 1] is True):
            # Horizontal run

            # Go backwards
            if x > 0:
                for tempX in range(x - 1, -1, -1):
                    if battleships[y][tempX] is False:
                        # Run ends
                        break
                    # Add to the number of hits if shot made
                    if shots[y][tempX] is True:
                        shipHits += 1
                    # Add to the ship length
                    shipLength += 1

            # Go forwards
            if x < 8:
                for tempX in range(x + 1, X_LENGTH):
                    if battleships[y][tempX] is False:
                        # Run ends
                        break
                    # Add to the number of hits if shot made
                    if shots[y][tempX] is True:
                        shipHits += 1
                    # Add to the ship length
                    shipLength += 1

        elif (y > 0 and battleships[y - 1][x] is True) or (y < 8 and battleships[y + 1][x] is True):
            # Vertical run

            # Go upwards
            if y > 0:
                for tempY in range(y - 1, -1, -1):
                    if battleships[tempY][x] is False:
                        # Run ends
                        break
                    # Add to the number of hits if shot made
                    if shots[tempY][x] is True:
                        shipHits += 1
                    # Add to the ship length
                    shipLength += 1

            # Go downwards
            if y < 8:
                for tempY in range(y + 1, Y_LENGTH):
                    if battleships[tempY][x] is False:
                        # Run ends
                        break
                    # Add to the number of hits if shot made
                    if shots[tempY][x] is True:
                        shipHits += 1
                    # Add to the ship length
                    shipLength += 1

        if shipLength == shipHits:
            shipsSunk += 1
            print("...a ship sinks!")

        print("=================================")

        # Check whether all ships have been sunk
        if shipsSunk == NUMBER_OF_SHIPS:
            print("All ships have been sunk!")
            break

    else:
        print("Missed.")

print("You shot {!s} missiles.".format(shotCount))
