class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if ((k==0) or (len(prices)<2)):
            return(0)
        
        import heapq
        diffs=[0]
        j=0
        while ((j<len(prices)-1) and (prices[j+1]<=prices[j])):
            j+=1
        if (j<(len(prices)-1)):
            diffs.append(prices[j+1]-prices[j])
        j+=1
        while ((j<len(prices)-1)):
            dif = prices[j+1]-prices[j]
            if (dif*diffs[-1] >= 1):
                diffs[-1] += dif
            elif (dif*diffs[-1] <= -1):
                diffs.append(dif)
            j+=1
        if (diffs[-1]<0):
            diffs.pop() # diffs should be bookkended by positives
        diffs.append(0)
        P = [(val,j) for (j,val) in enumerate(diffs) if (val>0)]
        N = [(-val,j) for (j,val) in enumerate(diffs) if (val<0)]
        num_excess_tx = len(P) - k
        heapq.heapify(P)
        heapq.heapify(N)
        for ii in range(num_excess_tx):
            while (diffs[P[0][1]]==0):
                heappop(P)
            while (diffs[N[0][1]]==0):
                heappop(N)
            if (P[0][0]<N[0][0]):
                (val,j) = heappop(P)
            else:
                (val,j) = heappop(N)
                val*=-1
            (L,R) = (j,j)
            while ((L>0) and (diffs[L]*val>=0)):
                L-=1
            while ((R<len(diffs)-1) and (diffs[R]*val>=0)):
                R+=1
            if ((diffs[L])*(diffs[R])==0): # edge case
                (diffs[L],diffs[R],diffs[j]) = (0,0,0)
            else: # interior case
                newValue = diffs[L]+diffs[R]+diffs[j]
                (diffs[L],diffs[R],diffs[j]) = (0,0,newValue)
                if (newValue>0):
                    heapq.heappush(P,(newValue,j))
                else:
                    heapq.heappush(N,(-newValue,j))
        return(sum([d for d in diffs if (d>0)]))