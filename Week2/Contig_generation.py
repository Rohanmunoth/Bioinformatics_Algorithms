import sys
from typing import List, Dict, Iterable, Tuple
import copy

# Please do not remove package declarations because these are used by the autograder.

# Insert your ContigGeneration function here, along with any subroutines you need
def ContigGeneration(Patterns: List[str]) -> List[str]:
    visitedNodes=set()
    path=[]
    nodes=set()
    g=Patterns
    m=dict()
    k=len(g[0])
    for i in g:
        if i[:k-1] not in m:
            m[i[:k-1]]=[i[1:]]
        else:
            m[i[:k-1]].append(i[1:])
    g=m
    in_df,out_df=check_InOut(g)
    for i in in_df:
        nodes.add(i)
    for i in out_df:
        if (i not in nodes):
            nodes.add(i)
    for i in nodes:
        if (i not in in_df):
            in_df[i]=0
        elif(i not in out_df):
            out_df[i]=0
    #print(g)
    #print(in_df,out_df)
    #print(nodes)
    for i in out_df:
        #print(i)
        if (in_df[i]!=1 or out_df[i]!=1):
            if (out_df[i]>0):
                #print(g[i])
                for j in g[i]:
                    visitedNodes.add(i)
                    nonBranchingPath=i
                    #print(j)
                    nonBranchingPath+=j[-1]
                    #print(nonBranchingPath)
                    newNode=j
                    while (in_df[newNode]==1 and out_df[newNode]==1):
                        visitedNodes.add(newNode)
                        for node in g[newNode]:
                            m=node
                        nonBranchingPath+=m[-1]
                        newNode=m
                    path.append(nonBranchingPath)
    #print(path)
    #print(visitedNodes)
        #elif (out_df[i]==1 and in_df[i]==1):
         #   for j in g[i]:
          #      node=j
           # nonBranchingPath=i+node[-1]
            #path.append(nonBranchingPath)
    for i in g:
        v=i
        if (v not in visitedNodes):
            nonBranchingPath=i
            while len(g[v])>0:
                if (v not in visitedNodes and (in_df[v]==1 or out_df[v]==1)):
                    visitedNodes.add(v)
                    #print(visitedNodes)
                    m=g[v][-1]
                    nonBranchingPath+=m[-1]
                    #print(nonBranchingPath)
                    v=g[v].pop()
            path.append(nonBranchingPath)    
    #print(path)   
    return path

def check_InOut(c):
    m=copy.deepcopy(c)
    out_df=dict()
    in_df=dict()
    for i in m:
        out_df[i]=len(m[i])
    for i in m:
        while m[i]:
            node=m[i].pop()
            if (node not in in_df):
                in_df[node]=1
            else:
                in_df[node]+=1
    return in_df, out_df
