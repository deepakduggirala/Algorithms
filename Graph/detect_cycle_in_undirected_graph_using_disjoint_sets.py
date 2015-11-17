from graph import unDGraph
def detectCycleUnDgraphDisjointSets(g):
    edges = []
    for u,edgeLst in enumerate(g.adjLst):   #assuming vertex numbers start from zero
        for v in edgeLst:
            if (v,u) not in edges:
                edges.append((u,v))
    print edges
    sets = [i for i in range(len(g.adjLst))]
    for u,v in edges:
        if sets[u] != sets[v]:
        #merge two sets and name the new set with higher node number
            setRepr = max(sets[u],sets[v])
            sets[u] = setRepr
            sets[v] = setRepr
        else:
            return True
    #print sets
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
