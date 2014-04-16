def quickSorting(a, start, end):
    if start >= end:
        return
    if len(a) == 0:
        return
    mid = (end - start) / 2 + start
    i = start
    j = end
    print i, j, mid
    #print a
    while i <= j:
        while a[i] < a[mid]:
            i += 1
        while a[j] > a[mid]:
            j -= 1
        if i <= j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i += 1
            j -= 1
        print a
    '''
    quickSorting(a, start, mid)
    quickSorting(a, mid, end)
    '''    
    if start < j:
        quickSorting(a, start, j)
    if i < end:
        quickSorting(a, i, end)
    

if __name__ == "__main__":
    a = [2,4,7,3,5,9,0]
    print a
    quickSorting(a, 0, len(a) - 1)
    print a

