def searchRange(A, target):
    if len(A) == 0:
        print [-1, -1]
        return
    if len(A) == 1:
        if A[0] == target:
            print [0, 0]
            return
        else:
            print [-1, -1]
            return
    if target < A[0] or target > A[-1]:
        print [-1, -1]
        return
    upBound = len(A) - 1
    lowBound = 0
    midPoint = 0
    flag = False
    
    while upBound >= lowBound:
        midPoint = (upBound + lowBound) // 2
        print upBound, lowBound, midPoint
        if A[midPoint] == target:
            flag = True
            break
        if A[midPoint] > target:
            upBound = midPoint - 1
        else:
            lowBound = midPoint + 1

    print midPoint
    print 'test'
    
    if flag == False:
        print [-1, -1]
        return
    lowBound = midPoint
    upBound = midPoint
    while A[lowBound] == target:
        lowBound -= 1
        print "lb", lowBound
        if lowBound < 0 or A[lowBound] != target:
            lowBound += 1 
            break
    while A[upBound] == target:
        upBound += 1
        print "ub", upBound
        if  upBound > len(A) - 1 or A[upBound] != target:
            upBound -= 1
            break
    print [lowBound, upBound]

if __name__ == "__main__":
	A = [1,4]
	target = 4
	searchRange(A, target)
