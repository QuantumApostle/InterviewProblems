import copy
def kSizeSubset(k, sol, totalSet, result, visited):
    if len(sol) == k:
        print 'k', k
        print 'sol', sol
        print 'visited', visited
        
        result.append(copy.deepcopy(sol))
        print 'result', result
        return
    else:
        for i in range(len(totalSet)):
            if visited[i] == 0:
                if len(sol) == 0 or sol[-1] < totalSet[i]:
                    visited[i] = 1
                    sol.append(totalSet[i])
                    kSizeSubset(k, sol, totalSet, result, visited)
                    visited[i] = 0
                    sol.pop()


if __name__ == "__main__":
    totalSet = [1,2]
    totalNum = len(totalSet)
    result = [[]]
    sol = []
    visited = []
    r = []
    for i in range(totalNum):
        visited.append(0)
    
    for k in range(1, totalNum + 1):
        kSizeSubset(k, sol, totalSet, result, visited)
        print result
    #print result

