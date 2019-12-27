class Solution:
    def canTransform(self, start, end):
        if start == end:
            return True
        
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        try:
            l1 = start.index('L')
            l2 = end.index('L')
        except ValueError:
            l1 = -1
            l2 = -1
        
        try:
            r1 = start.index('R')
            r2 = end.index('R')
        except ValueError:
            r1 = -1
            r2 = -1
        
        while (l1 != -1) or (r1 != -1):
            if (l1 >= l2) and (r1 <= r2):
                if l1 != -1:
                    try:
                        start = start.replace('L', '', 1)
                        end = end.replace('L', '', 1)
                        l1 = start.index('L')
                        l2 = end.index('L')
                    except ValueError:
                        l1 = -1
                        l2 = -1
                
                if r1 != -1:
                    try:
                        start = start.replace('R', '', 1)
                        end = end.replace('R', '', 1)
                        r1 = start.index('R')
                        r2 = end.index('R')
                    except ValueError:
                        r1 = -1
                        r2 = -1
            
            else:
                return False
        
        return True