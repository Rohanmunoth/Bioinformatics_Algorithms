def LongestPath(s,t,E):
    score =[float('-Inf')]*(t+1)
    score[s]=0
    paths=dict()
    for i in range (t+1):
        paths[i]=[]
    paths[s]=[s]
    for i in range (s,t+1):
        if i in E:
            for node,weight in E[i]:
                if score[node]<score[i]+weight:
                    score[node]=score[i]+weight
                    paths[node]=paths[i]+[node]
    return paths[t],score[t]



print(LongestPath(1,4,{1:[(2,1),(3,5)],2:[(4,10)],3:[(4,1)]}))
        
