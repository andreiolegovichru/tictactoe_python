#from IPython.display import clear_output

help_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
def clear_output():
    print('\n'*15);

def display_board(board):
    clear_output()
    print(f' | | \n{board[0]}|{board[1]}|{board[2]}\n | | \n-----\n | |\n{board[3]}|{board[4]}|{board[5]}\n | |\n-----\n | |\n{board[6]}|{board[7]}|{board[8]}\n | |')

valuelist2 = [0, 1, 2, 3, 4, 5, 6, 7, 8];
print('Please take a look at the desk positoins');
display_board(help_board)
print('You will need them for every new move');
board = [' '] * 9;
import random;

def choose_first():
    player_order = random.randint(1, 2);
    if player_order == 1:
        print('Player 1 makes first move');
    else:
        print('Player 2 makes first move');

def player_input():
    print('start');
    marker = False;
    while not marker:
        print('marker is 1 ', marker);
        player1marker = input("Please pick a marker 'X' or 'O','\n'");
        if player1marker.lower() == 'x':
            player1marker = 'X';
            player2marker = 'O';
            marker = True;
            #print('marker is 2 ', marker);
        elif player1marker.lower() == 'o':
            print('Player 1 marker is O');
            player1marker = 'O';
            player2marker = 'X';
            marker = True;
            #print('marker is 3 ', marker);
        else:
            print('Please enter the correct marker');

    return player1marker, player2marker;
#markers = player_input();


def space_check(board, position):
    # Returns True if the space is free
    if board[position - 1] == ' ':
        return True;
    else:
        return False;


def player_choice(board):
    check_box = False;
    # if game_over==True:
    #   check_box=True;
    while not check_box:
        print("Player");
        print('\n' * 3);
        local_position = int(input("move - type from 1 to 9\n"));
        print('\n'*3);
        if 1 <= local_position <= 9 and space_check(board, local_position) == True:
            check_box = True
        else:
            print('Please enter value between 1 and 9');
    return local_position;


def place_marker(board, marker, position1):
    board[position1 - 1] = marker;


def full_board_check(board):
 if " " in board[1:]:
     return False
 else:
     return True

def win_check(board, mark):
    for i in range(0, 9, 1):
        # print('win_check i= ',i);
        # print('win_check board[',i,']= ',board[i]);
        if i % 3 == 0 and board[i] == board[i + 1] == board[i + 2] == mark:
            # print('Line',i//3+1,'is filled with',mark);
            return True;
        elif i < 3 and (board[i] == board[i + 3] == board[i + 6] == mark):
            # print('Column',i+1,'is filled with',mark);
            return True;
        elif board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark:
            # print('Diagonal is filled');
            return True;
        elif i == 9:
            return False;
        else:
            i += 1;


def replay():
    want_more = input('Want to play again? Type Y or Yes if you do');
    w = want_more.lower();
    print(w);
    if w == 'yes' or w == 'y':
        return True;
    else:
        return False;


def rungame():
    board = [' '] * 9;
    markers = player_input();
    print('Player 1 marker is', markers[0], 'Player 2 marker is', markers[1]);
    game_over = False;
    # if game_over==True:
    # print("GAME OVER. Do you want to replay?");
    import random;
    choose_first();
    while not game_over:
        # print(game_over);
        # print(markers[0]);
        print('1111111111111111111111');
        position1 = player_choice(board);
        print('2222222222222222222222');
        space_check(board, position1);
        print('3333333333333333333333');
        place_marker(board, markers[0], position1);
        display_board(board);
        victory=win_check(board, markers[0])
        tie=full_board_check(board) and not victory;
        game_over = victory or tie;
        if victory:
            print('Victory!');
        if tie:
            print('Draw');
        if game_over:
            print("1111111111111111111111111111111111111111111111111111111111"
                  " \n|                                  \n|               GAME OVER. Do you want to replay?|              \n|"
                  "                                    "
                  "1111111111111111111111111111111111111111111111111111111111");
            if replay():
                print("REPLAY REQUESTED");
                rungame()
            else:
                print("THX and WELCOME AGAIN");
                exit()
        # print('Game over= ', game_over);
        position2 = player_choice(board);
        space_check(board, position2);
        place_marker(board, markers[1], position2);
        display_board(board);
        victory = win_check(board, markers[0])
        tie = full_board_check(board) and not victory;
        game_over = victory or tie;
        if victory:
            print('Victory!');
        if tie:
            print('Draw');
        if game_over:
            print(
                "----------------------------------- \n|                                  \n|               GAME OVER. Do you want to replay?|"
                "\n|"
                 "\n ----------------------------------- \n                                ");
            if replay():
                print("REPLAY REQUESTED");
                rungame()
            else:
                print("THX and WELCOME AGAIN");
                exit()
        else:
            pass;
#    gameover=win_check(board,markers[1]);
#   if game_over:
#      new_game=replay();
#     if new_game:
rungame()