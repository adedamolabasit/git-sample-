tic_board={'top-left':' ','top-mid':' ','top-right':' ',
           'mid-left':' ','mid-mid':' ','mid-right':' ',
           'low-left':' ','low-mid':' ','low-right':' '}
def showtacboard(board):
    print(f"{board['top-left']}|{board['top-mid']}|{board['top-right']}\n-------\n"
          f"{board['mid-left']}|{board['mid-mid']}|{board['mid-right']}\n-------\n"
          f"{board['low-left']}|{board['low-mid']}|{board['low-right']}")


turn='x'
for turn in range(9):
    showtacboard(tic_board)
    print(f'turn for {turn} move on which space?')
    move=input()
    tic_board[move]=turn
    if turn=='x':
        turn='0'
    else:
        turn='x'