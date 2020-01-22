class solution:

    def __init__(self, starting_height, stable_height, number_of_partitions):

        self.h0 = starting_height
        self.hmax = stable_height
        self.pilenum = number_of_partitions
    
    def main(self):

        h = [self.h0]
        while h[0] > self.hmax: 
            h = self.split(h)
        
        return len(h)
    
    def split(self, h):
        
        hmax = self.hmax
        pilenum = self.pilenum
        
        hnext =[]
        for hi in h:
            if hi > hmax:
                if hi > pilenum:
                    div = hi // pilenum
                    re = hi % pilenum
                    hnext = hnext + [div + re] + [div] * (pilenum - 1)
                else:
                    hnext = hnext + [1] * hi
            else:
                hnext = hnext + [hi]

        return hnext


starting_stack_size = 13
max_stable_height = 3
partition = 2
# starting_stack_size = 3
# max_stable_height = 2
# partition = 5
# starting_stack_size = 4
# max_stable_height = 3
# partition = 5

sol = solution(starting_stack_size, max_stable_height, partition)
print(sol.main())
