import copy
if __name__ == "__main__":
    num = [0,1,2,3]
    insertList = [[num[0]]]
    workList = []
    insertNum = 0
    p = 1
    for i in range(1, len(num)):
        p += 1
        insertNum = num[i]
        
        for l in insertList:            
            for j in range(p):
                workList.append(copy.deepcopy(l))                       
        for k in range(len(workList)):
            workList[k].insert(k % p, insertNum)
        
        insertList = []
        insertList = copy.deepcopy(workList)
        workList = []
    for l in insertList:
        print l
    
    
