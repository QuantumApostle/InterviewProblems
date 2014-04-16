def threeSum(num):
    num.sort()
    if len(num) < 3:
        print []
        return
    if len(num) == 3:
        if sum(num) == 0:
            print [num]
            return
        else:
            print []
            return
    i = 0
    j = 0
    k = 0
    res = []
        
    print 'num', num
    while i < len(num) - 2:
        j = i + 1
        k = len(num) - 1
        if num[i] + num[j] + num[j + 1] <= 0 or num[i] + num[k] + num[k - 1] >= 0:
            while j != k:
                sumValue = num[i] + num[j] + num[k]
                print 'sum', sumValue
                if sumValue == 0:
                    res.append([num[i], num[j], num[k]])
                    while j + 1 < len(num):
                        print 'j=', j
                        if num[j] == num[j + 1]:
                            j += 1
                        else:
                            j += 1
                            break
                    while k - 1 > j:
                        print 'k=', k
                        if num[k] == num[k - 1]:
                            k -= 1
                        else:
                            k -= 1
                            break
                elif sumValue < 0:
                    j += 1
                else:
                    k -= 1
                if j >= k:
                    break
                print j, k
        while i + 1 < len(num):
            if num[i] == num[i + 1]:
                i += 1
            else:
                break
        i += 1
        print i, j, k
    print res

if __name__ == "__main__":
    num = [-1,1,0]
    threeSum(num)
