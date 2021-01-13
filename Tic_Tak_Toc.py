#Tik_Tak_Toa game . It's a two player game. 
#Sudhakar N --- ^_^

board = ["-" for i in range(9)]


def displayBoard():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")


player1 = "x"
player2 = "o"


def conditions(player):
    Conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]
                  ]
    for check in Conditions:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return 1
    else:
        return 0


def Startgame():
    displayBoard()
    while True:
        while True:
            play_option1 = input(f"{player1} Enter the Position : ")
            if play_option1 not in [str(i) for i in range(1, 10)]:
                print("Please enter valid number [1-9]..")
                continue

            if board[int(play_option1) - 1] == "-":
                board[int(play_option1) - 1] = player1
                if conditions(player1):
                    print("---------------------")
                    print("---------------------")
                    displayBoard()
                    return f"{player1} is Winner"

                displayBoard()
                break
            else:
                print("This place not empty")

        if len([i for i in board if i == '-']) == 0:
            return 'Match Draw '
        while True:
            play_option2 = input(f"{player2} Enter the Position : ")
            if play_option2 not in [str(i) for i in range(1, 10)]:
                print("Please enter valid number [1-9]..")
                continue
            if board[int(play_option2) - 1] == "-":
                board[int(play_option2) - 1] = player2
                if conditions(player2):
                    print("---------------------")
                    print("---------------------")
                    displayBoard()
                    return f"{player2} is Winner"

                displayBoard()
                break
            else:
                print("This place not empty")


print(Startgame())

while True:
    option = input("Do you want to play again y-yes  n- No \n ")
    if option in 'yY':
        board = ["-" for i in range(9)]
        print(Startgame())
    else:
        exit()
