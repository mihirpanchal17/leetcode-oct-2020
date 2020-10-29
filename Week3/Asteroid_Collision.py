class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output=[]
        for i in asteroids:
            if not output or output[-1]<0 or i>0:
                output.append(i)
                continue
            else:
                while True:
                    if not output:
                        output.append(i) 
                        break
                    elif output[-1]<0:
                        output.append(i)
                        break
                    elif -i<output[-1]:
                        break
                    elif -i==output[-1]:
                        del output[-1]
                        break
                    else:
                        del output[-1]
        return output