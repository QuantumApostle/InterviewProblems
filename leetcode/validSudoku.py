def rowCheck(board):
    for i in range(9):
        dic = {}
        for j in range(9):
            if board[i][j] != '.':
                dic.setdefault(board[i][j], 0)
                dic[board[i][j]] += 1
        for key in dic.keys():
            if dic[key] > 1:
                return False
    return True

def colCheck(board):
    for i in range(9):
        dic = {}
        for j in range(9):
            if board[j][i] != '.':
                dic.setdefault(board[j][i], 0)
                dic[board[j][i]] += 1
        for key in dic.keys():
            if dic[key] > 1:
                return False
    return True

def blockCheck(board):
    row = 0
    col = 0
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            dic = {}
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    #print k, l
                    #print board[k][l]
                    if board[k][l] != '.':
                        dic.setdefault(board[k][l], 0)
                        dic[board[k][l]] += 1
            #print 'dic', dic
            for key in dic.keys():
                if dic[key] > 1:
                    print 'dic', dic
                    return False
    return True

if __name__ == "__main__":
	board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
	print rowCheck(board), colCheck(board),
	print blockCheck(board)
