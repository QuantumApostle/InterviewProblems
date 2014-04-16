import sys

def classifier(i, j, eMap, size, basinMap):
    up = sys.maxint
    down = sys.maxint
    left = sys.maxint
    right = sys.maxint
    middle = eMap[i][j]
    minValue = 0
    change = 0
    
    if i - 1 > -1:
        up = eMap[i - 1][j]

    if i + 1 < size:
        down = eMap[i + 1][j]

    if j - 1 > -1:
        left = eMap[i][j - 1]

    if j + 1 < size:
        right = eMap[i][j + 1]

    minValue = min([up, down, left, right, middle])
    print eMap[i][j], minValue
    if up == minValue:
        change = abs(basinMap[i][j] - basinMap[i - 1][j])
        basinMap[i][j] = basinMap[i - 1][j]
        
    if down == minValue:
        change = abs(basinMap[i][j] - basinMap[i + 1][j])
        basinMap[i][j] = basinMap[i + 1][j]
        
    if left == minValue:
        change = abs(basinMap[i][j] - basinMap[i][j - 1])
        basinMap[i][j] = basinMap[i][j - 1]
        
    if right == minValue:
        change = abs(basinMap[i][j] - basinMap[i][j + 1])
        basinMap[i][j] = basinMap[i][j + 1]
    return change
        

def findBasins(eMap, size):
    basins = []
    basinMap = []
    basins = {}
    n = 0
    change = 1
    
    for i in range(size):
        basinMap.append([])
        for j in range(size):
            basinMap[i].append(n)
            n += 1
    print basinMap
    
    while change != 0:
        change = 0
        for i in range(size):
            for j in range(size):
                change += classifier(i, j, eMap, size, basinMap)
    print basinMap
    for i in range(size):
        for j in range(size):
            basins.setdefault(basinMap[i][j], 0)
            basins[basinMap[i][j]] += 1
    for k in basins.keys():
        print basins
            
    
if __name__ == "__main__":
    eMap = [[1, 5, 2],[2, 4, 7],[3, 6, 9]]
    size = 3
    findBasins(eMap, size)
