class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        len_a = len(A)
        len_b = len(B)
        
        if len_a != len_b or set(A) != set(B): return False       
        if A == B:
            return len_a - len(set(A)) >= 1
        
        index = []
        for i in range(len_a):
            if A[i] != B[i]:
                index.append(i)
                if len(index) > 2:
                    return False
        if len(index) != 2:
            return False
        
        return A[index[0]]==B[index[1]] and A[index[1]]==B[index[0]]