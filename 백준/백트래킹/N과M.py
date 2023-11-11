N = 4
M = 2
arr = [0 for i in range(10)]
isused = [0 for i in range(10)]

def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end = ' ')
        print()
        return
    for i in range(1,N+1):
        if not isused[i]:
            arr[k] = i
            isused[i] = 1
            func(k+1)
            isused[i] = 0

func(0)