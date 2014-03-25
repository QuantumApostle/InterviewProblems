import copy
def genParth(l, r, s, returnList):
    print s
    if l == 0 and r == 0:
        
        returnList.append(s)
        
    if l > 0:
        genParth(l - 1, r, s + '(', returnList)
    
    if r > l:
        genParth(l, r - 1, s + ')', returnList)
    
    return returnList


if __name__ == "__main__":
    n = 2
    returnList = []
    s = ''
    result = genParth(n, n, s, returnList)
    print result

