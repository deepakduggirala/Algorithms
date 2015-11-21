from graph import unDGraph
from disjointSet import disjointSet
def detectCycleUnDgraphDisjointSets(g):
    edges = []
    sets = disjointSet(range(len(g.adjLst)))
    for u,edgeLst in enumerate(g.adjLst):   #assuming vertex numbers start from zero
        for v in edgeLst:
            if (v,u) not in edges:
                edges.append((u,v))
                if sets.find(u) != sets.find(v):
                #union two sets
                    sets.union(u,v)
                else:
                    return True
    return False
    
N = 6
g = unDGraph(N)
g.addEdge(0,5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,1)
#print g.adjLst
print detectCycleUnDgraphDisjointSets(g)
