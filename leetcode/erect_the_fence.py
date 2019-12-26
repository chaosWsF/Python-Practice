class Solution:
    def outerTrees(self, points):

        if len(points) < 3:
            return points
        
        def dfunc(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        
        def func(a, b, c):
            # get angle between vector BA and BC
            if (c == b) or (b == a):
                return 2
            else:
                return round(((b[0] - a[0])*(b[0] - c[0]) + (b[1] - a[1])*(b[1] - c[1])) / (dfunc(b, a) * dfunc(b, c)) ** .5, 10)
        
        def next_point(f1, f2, ps, pss, step_init=False):
            val_1s = [f1(p) for p in ps]
            val_1min = min(val_1s)
            nextps = [ps[i] for i, val_1 in enumerate(val_1s) if val_1 == val_1min]
            val_2s = [f2(p) for p in nextps]
            if step_init:
                if len(ps) == len(nextps):
                    sig = False
                else:
                    sig = True
                
                return nextps[val_2s.index(max(val_2s))], nextps, sig
            else:
                for nextp in nextps:
                    pss.append(ps.pop(ps.index(nextp)))
                
                if len(ps) == 0:
                    sig = False
                else:
                    sig = True

                return nextps[val_2s.index(max(val_2s))], sig

        pset = []

        func1 = lambda x: x[1]
        func2 = lambda x: x[0]
        p0, p0s, sig = next_point(func1, func2, points, pset, step_init=True)

        if sig:
            func1 = lambda x: func([p0[0] - 1, p0[1]], p0, x)
            func2 = lambda x: dfunc(x, p0)
            p1, sig = next_point(func1, func2, points, pset)
        else:
            pset.extend(p0s)
            return pset

        while sig:
            func1 = lambda x: func(p0, p1, x)
            func2 = lambda x: dfunc(x, p1)
            p2, sig = next_point(func1, func2, points, pset)
            
            if p2 in p0s:
                p0s.pop(p0s.index(p2))
                break

            p0 = p1
            p1 = p2

        pset.extend(p0s)
        return pset