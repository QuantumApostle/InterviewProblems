import copy
def generateMatrix(n):
    if n == 1:
        return [[1]]
    matrix = []
    row = []
    for i in range(n):
        row.append(0)
    for j in range(n):
        matrix.append(copy.deepcopy(row))
    numList = [x for x in range(1, n * n + 1)]
    i = 0
    j = 0
    d = 'right'
    #matrix[0][0] = 1
    for x in numList:
        matrix[i][j] = x
        if d == 'right':
            if i == 0 and j + 1 == n:
                d = 'down'
            else:
                if matrix[i][j + 1] != 0:
                    d = 'down'
        else:
            if d == 'down':
                if i + 1 == n and j + 1 == n:
                    d = 'left'
                else:
                    if matrix[i + 1][j] != 0:
                        d = 'left'
            else:
                if d == 'left':
                    if i + 1 == n and j == 0:
                        d = 'up'
                    else:
                        if matrix[i][j - 1] != 0:
                            d = 'up'
                else:
                    if d == 'up':
                        if matrix[i - 1][j] != 0:
                            d = 'right'
          
        if d == 'right':
            j += 1
        if d == 'down':
            i += 1
        if d == 'left':
            j -= 1
        if d == 'up':
            i -= 1
    return matrix
if __name__ == "__main__":
	mat = generateMatrix(5)
	for r in mat:
		print r
