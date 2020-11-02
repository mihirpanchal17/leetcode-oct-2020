class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur=[poured]
        for l in range(1,query_row+1):
            cur_=[0]*(l+1)
            for i in range(l):
                p=(cur[i]-1)/2
                if p<0: continue
                cur_[i]+=p
                cur_[i+1]+=p
            cur=cur_
        return cur[query_glass] if cur[query_glass]<1 else 1