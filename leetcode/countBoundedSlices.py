import sys
def boundedSlicesSlow(K, A):
    N = len(A)
    result = 0
    for i in xrange(N):
        minimum = A[i]
        maximum = A[i]
        for j in xrange(i, N):
            maximum = max(maximum, A[i])
            minimum = min(minimum, A[j])
            if maximum - minimum <= K:
                result += 1
                if result == sys.maxint:
                    return result
            else:
                break
    return result
    
if __name__ == "__main__":
    A = [3, 5, 7, 6, 3]
    K = 2
    print boundedSlicesSlow(K, A)
