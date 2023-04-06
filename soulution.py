while True:
    try:
        n,m = map(int,input().split())
    except:
        break
    a = []
    for i in range(n):
        b = list (map(int,input().split()))
        a.append(b)

