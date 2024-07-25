import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your genome_path function here, along with any subroutines you need
def genome_path(path: List[str]) -> str:
    k_mer=len(path[0])
    sequence=path[0]
    path.pop(0)
    i=0
    while len(path)>0:
        if (sequence[len(sequence)-k_mer+1:]==path[i][:k_mer-1]):
            sequence+=path[i][k_mer-1]
            path.pop(i)
            i=0
        elif (sequence[len(sequence)-k_mer+1:]==path[i][1:]):
            sequence=path[i][k_mer-1]+sequence
            path.pop(i)
            i=0
        else:
            i+=1
    return sequence 
    """Forms the genome path formed by a collection of patterns."""