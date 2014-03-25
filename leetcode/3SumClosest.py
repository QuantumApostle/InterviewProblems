import copy
def getAllThreeSums(sol, result, visited, num):
    if len(sol) == 3:
        result.append(sum(sol))
        return
    else:
        for i in range(len(num)):
            if visited[i] == 0:
                if len(sol) == 0 or sol[-1] < num[-1]:
                    visited[i] = 1
                    sol.append(num[i])
                    getAllThreeSums(sol, result, visited, num)
                    visited[i] = 0
                    print sol
                    sol.pop()


if __name__ == "__main__":
    num = [-1, 2, 1, -4]
    num.sort()
    target = 1
    sol = []
    result = []

    visited = []
    for i in range(len(num)):
        visited.append(0)
    getAllThreeSums(sol, result, visited, num)
    print result
    dist = 100000
    r3Sum = 0
    for r in result:
        if dist >= abs(r - target):
            print dist
            dist = abs(r - target)
            r3Sum = r
    print 'res=',r3Sum

