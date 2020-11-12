#lets creat an empty list
print("you can access the box by representing its index values")
print("    0 1 2")
print("    ^ ^ ^ ")
print("    | | | ")
print("   -------")
print("0->| | | |")
print("   -------")
print("1->| | | |")
print("   -------")
print("2->| | | |")
print("   -------")

board=[[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]
        
def monitor():
    
    global board
    
    for i in range(0,3): # to check horizontal
        if board[i][0] == "X"  and board[i][1] == "X" and board[i][2]=="X":
            print("player1 won the match")
            return 1
        elif board[0][i] == "X"  and board[1][i] == "X" and board[2][i] =="X":#check vertical
            print("player1 won the match")
            return 1
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("player1 won the match")
        return 1
    if board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("player1 won the match")
        return 1
    
    for i in range(0,3): # to check horizontal
        if board[i][0] == "O"  and board[i][1] == "O" and board[i][2]=="O":
            print("player2 won the match")
            return 1
        elif board[0][i] == "O"  and board[1][i] == "O" and board[2][i] =="O":#check vertical
            print("player2 won the match")
            return 1
    if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("player2 won the match")
        return 1
    if board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
        print("player2 won the match")
        return 1
    return 0

def print_board():
    global board
    for i in range(0,3):
        
        print("-------------")
        line='| '
        for j in range(0,3):
            line += ''
            line += board[i][j]+" | " 
        print(line)
    print("-------------")
print_board()

end_move = 0
player = 1
total_moves=0
while True:
    end_move = monitor()
    if total_moves == 9 or end_move==1:
        break
    while True:
        if player == 1:
            p1_input = input("player one ")
            a = int(p1_input[0])
            b = int(p1_input[1])
            if a < 3 and b < 3:

                if board[a][b] == " ":
                    board[a][b] = "X"
                    print_board()
                    player = 2
                    break
                else:
                    print("invalid input, try again ")
                    continue
            else:
                print("Value out of range")
        else:
            if a < 3 and b < 3:
                p2_input = input("player two ")
                c = int(p2_input[0])
                d = int(p2_input[1])
                if board[c][d] == " ":
                    board[c][d] = "O"
                    print_board()
                    player = 1
                    break
                else:
                    print("invalid input, try again ")
                    continue
            else:
                print("Value out of range")
    total_moves += 1



