class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        number_of_bits = (int)(math.floor(math.log(N) / math.log(2))) + 1; 
  
        return ((1 << number_of_bits) - 1) ^ N;