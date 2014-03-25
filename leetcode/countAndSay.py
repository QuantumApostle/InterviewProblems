import copy
def countAndSay(n):
    if n == 1:
        return "1"
    workList = [1]
    res = []
    
    count = 0
    for i in range(n - 1):
        
        for j in range(len(workList)):
            count += 1
            if j + 1 == len(workList):
                res.append(count)
                res.append(workList[j])
                break
            if workList[j] != workList[j + 1]:
                res.append(count)
                res.append(workList[j])
                count = 0
        count = 0
        workList = copy.deepcopy(res)
        res = []
        print 'workList = ', workList
    result = ""
    for digit in workList:
        result += str(digit)
    return result
    
if __name__ == "__main__":
    
    print countAndSay(3)	
