class SegmentTree():
    def __init__(self, arr, merge):
        self.arr = arr
        self.n = len(self.arr)
        self.merge = merge
        self.height_ = int(math.ceil(math.log2(self.n)))
        self.capacity_ = 2*int(math.pow(2, self.height_))-1
        self.st = [0]*self.capacity_
        self.make_segment_tree(0, self.n-1, 0)
    
    def make_segment_tree(self, start_i, end_i, st_root):
        if start_i == end_i:
            self.st[st_root] = self.arr[start_i]
        else:
            mid_i = start_i + (end_i - start_i)//2
            l_root = st_root*2+1
            r_root = st_root*2+2
            l = self.make_segment_tree(start_i, mid_i, l_root)
            r = self.make_segment_tree(mid_i+1, end_i, r_root)
            self.st[st_root] = self.merge(l, r)

        return self.st[st_root]
    
    def query(self, qs, qe):
        if qs < 0 or qe > self.n-1 or qs > qe:
            return None
        return self.query_(qs, qe, 0, self.n-1, 0)
    
    def query_(self, qs, qe, ss, se, st_root):
        '''
        qs: query start index
        qe: query end index
        
        0 <= qs <= qe < n - this is verified
        
        ss: segment start index of the current tree
        se: segment end index of the current tree
        st_root: index of the current tree
        '''
        
        # if the given interval is bigger than and overlaps with the current segment tree range (  qs ss se qe  )
        if qs <= ss and qe >= se:
            return self.st[st_root]
        
        # range of the current tree and query interval are disjoint (  qs qe ss se, ss se qs qe  )
        if qe < ss or qs > se:
            return None
        
        # part of the query interval overlaps with the current tree's range (  ss qs se qe, qs ss qe se  )
        # or
        # current tree range is bigger than and overlaps with the query interval (  ss qs qe se  )
        mid_i = ss + (se - ss)//2
        l_root = st_root*2 + 1
        r_root = st_root*2 + 2
        
        l_val = self.query_(qs, qe, ss, mid_i, l_root)
        r_val = self.query_(qs, qe, mid_i+1, se, r_root)
        
        if l_val is None:
            return r_val
        if r_val is None:
            return l_val
        
        return self.merge(l_val, r_val)
    
    def update(self, i, new_val):
        if 0 <= i and i < self.n:
            self.arr[i] = new_val
            self.update_(i, i, 0, self.n-1, 0)
        
    def update_(self, qs, qe, ss, se, st_root):
        print(qs, qe, ss, se, st_root)
        # range of the current tree and query interval are disjoint (  qs qe ss se, ss se qs qe  )
        if qe < ss or qs > se:
            return self.st[st_root]
        if qs==ss and qe==se:
            return self.arr[ss]
        
        mid_i = ss + (se - ss)//2
        l_root = st_root*2 + 1
        r_root = st_root*2 + 2
        
        l_val = self.update_(qs, qe, ss, mid_i, l_root)
        r_val = self.update_(qs, qe, mid_i+1, se, r_root)
        
        self.st[st_root] = self.merge(l_val, r_val)
        return self.st[st_root]
        
        
st = Segment_tree([1, 3, 5, 7, 9, 11], lambda x,y: x+y)
st.query(0,1)