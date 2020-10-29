class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a, ac = Counter(A).most_common(1)[0]
        b, bc = Counter(B).most_common(1)[0]
        count = 0
        if ac > bc:
            for i in range(len(A)):
                if A[i] != a:
                    A[i], B[i] = B[i], A[i]
                    count += 1
            return count if len(set(A)) == 1 else -1
        else:
            for i in range(len(B)):
                if B[i] != b:
                    B[i], A[i] = A[i], B[i]
                    count += 1
            return count if len(set(B)) == 1 else -1