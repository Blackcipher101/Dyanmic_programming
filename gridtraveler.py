def gridTravler(m,n,memo={}):
    key = str(m)+","+str(n)
    if (key) in memo:
        print (memo[key])
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = gridTravler(m-1,n,memo) + gridTravler(m,n-1,memo)
    return memo[key]


print(gridTravler(18,18))
