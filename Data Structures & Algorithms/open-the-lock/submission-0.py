class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        q = deque()
        q.append(["0000", 0])
        visited = set()

        while len(q) != 0:
            cur = q.popleft()
            cur_val = cur[1]
            cur_lock = cur[0]
            if cur_lock in deadends or cur_lock in visited:
                continue
            
            if cur_lock == target:
                return cur_val

            visited.add(cur_lock)
            for i in range(4):
                temp_1 = str((int(cur_lock[i])+11) % 10) #Increment up
                temp_2 = str((int(cur_lock[i])+9) % 10) #Incremment down
                new_1 = cur_lock[:i] + temp_1 + cur_lock[i+1:]
                new_2 = cur_lock[:i] + temp_2 + cur_lock[i+1:]
                q.append([new_1, cur_val+1])
                q.append([new_2, cur_val+1])

        return -1