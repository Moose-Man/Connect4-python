# Make Connect 4, a game in which four zeroes in a 2D array must be lined up in a row, whether it is diagonal, horizontal or vertical.


# SET UP = CREATE THE TABLE + OTHER VARIABLES

ConnectTable = [[1 for Column in range(7)] for Row in range(6)]
Placed = False
win = False
diskLocation = 0
disk = 0
turn = -1
# CREATE MENU

print("Play Connect4? (yes/no)")
answer = input()

while answer != "yes" and answer != "no":
    print("Type yes or no please.")
    answer = input()

if answer == "no":
    print("Well why did you open this program then.")
else:

# START GAME -  ASK FOR USER INPUT(creating loop of ALL following code as well)

    while win == False:
        Placed = False
        turn = turn+1
        if (turn % 2) == 0:
            print("Player One Turn")
            disk = 0
        else:
            print("Player Two Turn")
            disk = 2

        print("in which column would you like to place a disk?")
        diskLocation = int(input())-1
        while diskLocation < 0 or diskLocation > 6:
            print("please enter a number from 1 to 7 inclusive")
            diskLocation = int(input())-1

    # CHECK IF COL HAS SPACE FOR ENTRY AND ADD DISK IN SELECTED COLUMN

        for counter in range(6):
             print(counter)
             if counter < 6 and counter > 0 and Placed is False:
                 if ConnectTable[counter][diskLocation] != 1:
                     ConnectTable[counter-1][diskLocation] = disk
                     Placed = True
                     diskRow = counter-1
                  # Check if the final space is taken. If so, add the disk in the space above.
                 elif ConnectTable[5][diskLocation] != 1 and ConnectTable[4][diskLocation] == 1:
                     ConnectTable[4][diskLocation] = disk
                     diskRow = 4
                     Placed = True
                     # if not, place in the final space
                 elif Placed is False and counter == 5:
                     ConnectTable[5][diskLocation] = disk
                     diskRow = 5
                     Placed = True



    # PRINT NEW AND CHANGED CONNECT TABLE
        for row in range(len(ConnectTable)):
            print(ConnectTable[row])

# CHECK IF 4 ARE CONNECTED (H)

        for counter in range(6):
            if win == False:
                if ConnectTable[diskRow][counter] == disk:
                    if ConnectTable[diskRow][counter+1] == disk and counter < 5:
                        if ConnectTable[diskRow][counter+2] == disk and counter < 4:
                            if ConnectTable[diskRow][counter+3] == disk:
                                if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                                else:
                                    print("player 2 Wins!")
                                    win = True

#CHECK IF 4 ARE CONNECTED (V)


        for counter in range (5):
            if win == False:
                if ConnectTable[counter][diskLocation] == disk and counter < 5:
                    if ConnectTable[counter+1][diskLocation] == disk and counter < 4:
                        if ConnectTable[counter+2][diskLocation] == disk and counter < 3:
                            if ConnectTable[counter+3][diskLocation] == disk:
                                if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                                else:
                                    print("player 2 Wins!")
                                    win = True

#CHECK IF 4 ARE CONNECTED (D-RIGHT-UP)

        for counter in range (5):
            if win == False and diskLocation != 6:
                if ConnectTable[counter][diskLocation] == disk and counter < 5:
                    if ConnectTable[counter+1][diskLocation+1] == disk and counter < 4:
                        if ConnectTable[counter+2][diskLocation+2] == disk and counter < 3:
                            if ConnectTable[counter+3][diskLocation+3] == disk:
                                if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                                else:
                                    print("player 2 Wins!")
                                    win = True

#CHECK IF 4 ARE CONNECTED (D-LEFT-UP)

        for counter in range (5):
            if win == False:
                if ConnectTable[counter][diskLocation] == disk and counter < 5:
                    if ConnectTable[counter+1][diskLocation-1] == disk and counter < 4:
                        if ConnectTable[counter+2][diskLocation-2] == disk and counter < 3:
                            if ConnectTable[counter+3][diskLocation-3] == disk:
                              if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                              else:
                                    print("player 2 Wins!")
                                    win = True

#CHECK IF 4 ARE CONNECTED (D-RIGHT-DOWN)

        for counter in range (5):
            if win == False and diskLocation != 6:
                if ConnectTable[counter][diskLocation] == disk and counter > 0:
                    if ConnectTable[counter-1][diskLocation+1] == disk and counter > 1:
                        if ConnectTable[counter-2][diskLocation+2] == disk and counter > 2:
                            if ConnectTable[counter-3][diskLocation+3] == disk:
                                if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                                else:
                                    print("player 2 Wins!")
                                    win = True

#CHECK IF 4 ARE CONNECTED (D-LEFT-DOWN)

        for counter in range (5):
            if win == False:
                if ConnectTable[counter][diskLocation] == disk and counter > 0:
                    if ConnectTable[counter-1][diskLocation-1] == disk and counter > 1:
                        if ConnectTable[counter-2][diskLocation-2] == disk and counter > 2:
                            if ConnectTable[counter-3][diskLocation-3] == disk:
                                if (turn % 2) == 0:
                                    print("player 1 Wins!")
                                    win = True
                                else:
                                    print("player 2 Wins!")
                                    win = True


