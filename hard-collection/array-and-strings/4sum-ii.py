class Solution(object):
    
    def fourSumCount(self, A, B, C, D):
        N = len(A)
        cache = {}
        for i in range (N):
            for j in range(N):
                res = A[i] + B[j]
                if res not in cache:
                    cache[res] = 1
                else:
                    cache[res] += 1
        count = 0
        for i in range(N):
            for j in range(N):
                res = -1 * (C[i] + D[j])
                if res in cache:
                    count += cache[res]
        
        return count