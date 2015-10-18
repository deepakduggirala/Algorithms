import heapq
T = int(raw_input())
for t in xrange(T):
    N,M = tuple(map(int,raw_input().strip().split()))
    a = [[] for i in range(N+1)]
    for i in xrange(M):
        x,y,r = tuple(map(int,raw_input().strip().split()))
        a[x].append((y,r))
        a[y].append((x,r))
    Visited = [False for i in range(N+1)]
    Distance = [float('inf') for i in range(N+1)]
    S = int(raw_input())
    Distance[S] = 0
    heap = []
    heapq.heappush(heap,(0,S))
    for i in xrange(1,N+1):
        if heap:
            while(True):
                _,u = heapq.heappop(heap)
                if not Visited[u]:
                    break
            Visited[u] = True
            for v,weight_uv in a[u]:
                if not Visited[v]:
                    if Distance[v] > Distance[u] + weight_uv:
                        Distance[v] = Distance[u] + weight_uv
                        heapq.heappush(heap, (Distance[v],v))
    for i in range(N+1):
        if Distance[i] == float('inf'):
            Distance[i] = -1
    print ' '.join(map(str,Distance[1:S]+Distance[S+1:]))+' '
