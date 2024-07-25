import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_kmers function here, along with any subroutines you need
def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    graph=dict()
    lenght=len(k_mers[0])
    for i in range (len(k_mers)):
        suffix=k_mers[i][:lenght-1]
        prefix=k_mers[i][1:lenght]
        if (suffix not in graph):
            graph[suffix]=[prefix]
        elif (suffix in graph):
            graph[suffix].append(prefix)
    return graph
        
    """Forms the de Bruijn graph of a collection of k-mers."""