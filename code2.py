def polynomial(x,li):
    sm = 0
    j = 0
    for i in range(len(li)-1,-1,-1):
        sm += li[i]*(x**j)
        j += 1
    return sm

n = int(input())
arr = list(map(int,input().split()))
print(polynomial(n,arr))
