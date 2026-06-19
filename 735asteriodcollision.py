class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq = deque([])

        ans = []
        idx = 0

        while idx < len(asteroids):

            if asteroids[idx] < 0:

                # Remove all elements that this asteriod will destroy.
                while len(dq) > 0 and dq[-1] < -asteroids[idx]:
                    dq.pop()

                # If something left then its either equal or more.
                if len(dq) > 0 and dq[-1] == -asteroids[idx]:
                    dq.pop()
                    idx += 1
                    continue

                if len(dq) == 0:
                    # if length is zero then it means that all asteriods are destroyed.
                    ans.append(asteroids[idx])
            
            else:
                dq.append(asteroids[idx])
            
            idx += 1

        while len(dq) > 0:
            # Assign all asteriods that were not able to be destroyed.
            ans.append(dq.popleft())
        
        return ans
