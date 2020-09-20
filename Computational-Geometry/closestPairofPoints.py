random_points = sorted([(x,y)for x,y in np.random.random((5,2))]) 

def dist(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return math.sqrt((p2x-p1x)**2 + (p2y-p1y)**2)

def closest_pair_of_points_brute_force(points):
    dmin = math.inf
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dmin = min(dmin, dist(points[i], points[j]))
    return dmin

def closest_pair_of_points(points):
    if len(points) == 3:
        ab = dist(points[0], points[1])
        bc = dist(points[1], points[2])
        ca = dist(points[2], points[0])
        return min(ab, bc, ca)
    if len(points) == 2:
        return dist(points[0], points[1])
    
    # separate points into two halves based on x median
    x_median_i = len(points)//2
    x_median = points[x_median_i][0]
    
    left_points = points[:x_median_i]
    right_points = points[x_median_i:]
  
    # divide and conquer
    lmin = closest_pair_of_points(left_points)
    rmin = closest_pair_of_points(right_points)
    
    # find points whose x values are in the range x_median-min(lmin, rmin) <= x <= x_median+min(lmin, rmin)
    l_points_dist = [(x,y) for x,y in left_points if (x_median - x) <= min(lmin, rmin)]
    r_points_dist = [(x,y) for x,y in right_points if (x - x_median) <= min(lmin, rmin)]
    
    lrdmin = math.inf
    
    # even though this looks quadratic, it is linear since atmost 6 points can exist in the rectangle d, 2*d on one side of the separating line for any value of n
    # d is min(lmin, rmin)
    # What is the maximum number of points that can be arranged such that they are separated by distance d in 2d plane??
    for lp in l_points_dist:
        lx, ly = lp
        for rp in r_points_dist:
            rx, ry = rp
            if ly-min(lmin, rmin) <= ry and ry <= ly+min(lmin, rmin):
                lrdmin = min(lrdmin, dist(lp, rp))
    
    return min(lrdmin, lmin, rmin)
        
    
closest_pair_of_points_brute_force(random_points), closest_pair_of_points(random_points)


def merge_k_max_heaps(heap1, heap2, k):
    # worst case complexity is O(klogk)
    small_heap, big_heap = None, None
    if len(heap1) < len(heap2):
        small_heap, big_heap = heap1, heap2
    else:
        small_heap, big_heap = heap2, heap1
    for i in small_heap:
        k_max_heap_insert(big_heap, k, i)
    return big_heap

def k_max_heap_insert(heap, k, i):
    if len(heap) < k:
        heapq.heappush(heap, i)
    else:
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)
    return heap

def k_closest_pair_of_points(points, k):
    if len(points) == 3:
        ab = dist(points[0], points[1])
        bc = dist(points[1], points[2])
        ca = dist(points[2], points[0])
        
        dist3 = [ab, bc, ca]
        neg_dist3 = [-d for d in dist3]
        heapq.heapify(neg_dist3)
        return (neg_dist3, min(dist3)) # at-most k-sized max heap
    
    if len(points) == 2:
        d = dist(points[0], points[1])
        return ([-d], d) # at-most k-sized max heap
    
    # separate points into two halves based on x median
    x_median_i = len(points)//2
    x_median = points[x_median_i][0]
    
    left_points = points[:x_median_i]
    right_points = points[x_median_i:]
  
    # divide and conquer
    l_heap, lmin = k_closest_pair_of_points(left_points, k)
    r_heap, rmin = k_closest_pair_of_points(right_points, k)
    k_smallest = merge_k_max_heaps(l_heap, r_heap, k) # max-heap of at-most k size
    
    # find points whose x values are in the range x_median-min(lmin, rmin) <= x <= x_median+min(lmin, rmin)
    l_points_dist = [(x,y) for x,y in left_points if (x_median - x) <= min(lmin, rmin)]
    r_points_dist = [(x,y) for x,y in right_points if (x - x_median) <= min(lmin, rmin)]
    
    lrdmin = math.inf
    
    # even though this looks quadratic, it is linear since atmost 6 points can exist in the rectangle d, 2*d on one side of the separating line for any value of n
    # d is min(lmin, rmin)
    # What is the maximum number of points that can be arranged such that they are separated by distance d in 2d plane??
    for lp in l_points_dist:
        lx, ly = lp
        for rp in r_points_dist:
            rx, ry = rp
            if ly-min(lmin, rmin) <= ry and ry <= ly+min(lmin, rmin):
                lrdmin = min(lrdmin, dist(lp, rp))
    
    k_max_heap_insert(k_smallest, k, -lrdmin)
    
    return (k_smallest ,min(lrdmin, lmin, rmin))
