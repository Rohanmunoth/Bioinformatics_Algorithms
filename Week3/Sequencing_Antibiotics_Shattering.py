def circular(g):
    final=[]
    c=1
    scores=[]
    string=''
    for i in range (len(g)):
        for j in range (len(g)):
            if ((j+c)<len(g)):
                m=g[j:j+c]
            else:
                m=g[j:]+g[:(j+c-len(g))]
            if (len(m)!=len(g)):
                final.append(m)
        c+=1
    (final.append(g))
    for i in final:
        scores.append(score(i))
    scores=[0]+scores
    scores=sorted(scores)
    for i in scores:
        string+=str(i)+' '
    return string

def score(string):
    scores=0
    mass_values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y': 163,'W': 186}
    for i in string:
        scores+=mass_values[i]
    return scores

print(circular('LNEQ'))