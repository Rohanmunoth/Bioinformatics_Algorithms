def LongestPathLength(n: int, m: int,
                      Down, Right):
    down=Down
    right=Right
    s=[[0]*(m+1) for i in range(n+1)]
    s[0][0]=0
    for i in range (1,n+1):
        s[i][0]=s[i-1][0]+down[i-1][0]
    for j in range (1,m+1):
        s[0][j]=s[0][j-1]+right[0][j-1]
    for i in range (1,n+1):
        for j in range (1,m+1):
            s[i][j]=max(s[i-1][j]+down[i-1][j],s[i][j-1]+right[i][j-1])
    return s[n][m]