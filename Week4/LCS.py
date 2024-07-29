def outputLCS(backTrack,v,i,j):
    if i==0 or j==0:
        return ''
    if backTrack[j][i]=='Down':
        return outputLCS(backTrack,v,i,j-1)
    elif backTrack[j][i]=='Right':
        return outputLCS(backTrack,v,i-1,j)
    elif backTrack[j][i]=='Diagonal':
        return outputLCS(backTrack,v,i-1,j-1)+v[i-1]

def LCSBacktrack(v,w):
    s=[[0]*(len(v)+1) for i in range (len(w)+1)]
    Backtrack=[['']*(len(v)+1) for i in range (len(w)+1)]
    for i in range (len(v)+1):
        s[0][i]=0
    for j in range (len(w)+1):
        s[j][0]=0
    for i in range (1,len(v)+1):
        for j in range (1,len(w)+1):
            match =0
            if v[i-1]==w[j-1]:
                match=1
            s[j][i]=max (s[j-1][i],s[j][i-1],s[j-1][i-1]+match)
            if s[j][i]==s[j-1][i]:
                Backtrack[j][i]='Down'
            elif s[j][i]==s[j][i-1]:
                Backtrack[j][i]='Right'
            elif s[j][i]==s[j-1][i-1]+match:
                Backtrack[j][i]='Diagonal'
    return outputLCS(Backtrack,v,len(v),len(w))
    
print(LCSBacktrack('GACT','ATG'))