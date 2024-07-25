import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your eulerian_cycle function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u
def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    current_node=[]
    current_cycle=[]
    v=next(iter(g))
    current_node.append(v)
    while current_node:
        if g[v]:
            current_node.append(v)
            v=g[v].pop()
        else:
            current_cycle.append(v)
            v=current_node.pop()
    return current_cycle[::-1]
    """Constructs an Eulerian cycle in a graph."""
