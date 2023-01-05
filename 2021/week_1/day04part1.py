with open('../input/day04_input.txt', 'r') as f:
    input = f.readlines()

numbers_to_draw = input[0].strip().split(',')
boards = []
for i in range(0, len(input), 6):
    try:
        boards.append([line.strip().split() for line in input[i+2:i+7]])
    except:
        break
boards.pop()
scores = []
for board in boards:
    scores.append([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]])

def bingo(scores):
    for b in range(len(scores)):
        for i in range(5):
            if sum(scores[b][i]) == 5 or\
                    scores[b][0][i]+scores[b][1][i]+scores[b][2][i]+scores[b][3][i]+scores[b][4][i] == 5:
                return b
    return None


def remaining(board, score):
    rem = 0
    for r in range(5):
        for c in range(5):
            rem += int(board[r][c])*abs(score[r][c]-1)
    return rem


for number in numbers_to_draw:
    for b in range(len(boards)):
        for r in range(5):
            for c in range(5):
                if boards[b][r][c] == number:
                    scores[b][r][c] = 1
    winning_board = bingo(scores)
    if winning_board:
        print(int(number) * remaining(boards[winning_board], scores[winning_board]))
        break


