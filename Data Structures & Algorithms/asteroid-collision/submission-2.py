class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            done = False
            if i > 0:
                stack.append(i)

            elif len(stack) == 0 or stack[-1] < 0:
                stack.append(i)
            
            else:
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] < 0 and i < 0:
                        continue
                    if abs(stack[j]) < abs(i):
                        stack.pop()
                    elif abs(stack[j]) == abs(i):
                        done = True
                        stack.pop()
                        break
                    else:
                        done = True
                        break
                
                if done == False:
                    stack.append(i)
                

        return stack