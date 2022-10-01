
def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):

    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)


    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):

    wins = [[0, 1, 2], [0, 3, 6], [2, 5, 8], [6, 7, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the match !")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the match !")
            return 0

    return -1

if __name__ == "__main__":
    xState = [0 for _ in range(10)] # [0,0,0,0,0,0,0,0,0]
    zState = [0 for _ in range(10)]
    turn = 1 # it's value will be 1 if it's X's turn else value -> 0
    print("Tic Tac Toe")

    while 1:
        printBoard(xState, zState)

        if(turn == 1):
            print("X's turn")
            value = int(input("Please enter a value\n"))
            xState[value] = 1
        else:
            print("O's turn")
            value = int(input("Please enter a value\n"))
            zState[value] = 1

        # checking the winner
        win = checkWin(xState, zState)
        if(win != -1):
            break
        
        # changing the turn of players
        turn = 1 - turn
