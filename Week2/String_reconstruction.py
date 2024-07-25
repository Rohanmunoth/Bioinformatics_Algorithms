import sys
import copy
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your string_reconstruction function here, along with any subroutines you need
def string_reconstruction(patterns: List[str], k: int) -> str:
    g=patterns
    m=dict()
    for i in g:
        if i[:k-1] not in m:
            m[i[:k-1]]=[i[1:]]
        else:
            m[i[:k-1]].append(i[1:])
    g=m
    g,first_node,last_node=check_InOut(g)
    current_node=[]
    current_cycle=[]
    v=next(iter(g))
    current_node.append(v)
    while current_node:
        if g[v]:
            #print(current_node)
            current_node.append(v)
            v=g[v].pop()
        else:
            current_cycle.append(v)
            v=current_node.pop()
    current_cycle=current_cycle[::-1]
    for i in range (len(current_cycle)-1):
        if (current_cycle[i]==last_node and current_cycle[i+1]==first_node):
            current_cycle=current_cycle[i+1:]+current_cycle[1:i+1]
            break
    final_string=current_cycle[0]
    m=0
    for i in current_cycle:
        if m>0:
            final_string=final_string+i[len(i)-1]
        m+=1
    return (final_string)

def check_InOut(m):
    final_dict=copy.deepcopy(m)
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
    first_node,last_node=balance_node(out_df,in_df)
    if (last_node not in final_dict and first_node!=None and last_node!=None) :
        final_dict[last_node]=[first_node]
    elif (last_node in final_dict and first_node!=None and last_node!=None):
        final_dict[last_node].append(first_node)
    return final_dict,first_node,last_node

def balance_node(out_df,in_df):
    first_node=None
    last_node=None
    for i in out_df:
        if (i not in in_df or out_df[i]>in_df[i]):
            first_node=i
    for i in in_df:
        if (i not in out_df or in_df[i]>out_df[i]):
            last_node=i
    return first_node,last_node

    """Reconstructs a string from its k-mer composition."""