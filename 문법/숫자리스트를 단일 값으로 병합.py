
a = [1,2,3,4,5] # 처럼 숫자형으로 이루어진 리스트를 하나로 합치는 코드
b = [6,7,8,9,10]

# 1
''.join(str(e) for e in a)

# 2
''.join(map(str,a))

# 1-1
resultStr = int(''.join(str(e) for e in a)) + \
    int(''.join(str(e) for e in b))

# 2-1
resultStr = int(''.join(map(str,a))) + \
    int(''.join(map(str,b)))


functools.reduce(lambda x, y: 10 * x + y, a, 0)