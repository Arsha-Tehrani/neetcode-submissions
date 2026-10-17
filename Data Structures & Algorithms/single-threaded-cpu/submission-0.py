class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(reverse = True) #Reverse sort so you can use pop
        res = []
        seq = []
        n = len(tasks) #Save original number of items

        time = tasks[-1][0] #go to closest task
        while len(res) < n:
            t = len(tasks) #amount of time to repeat
            for i in range(t, 0, -1):
                if tasks[-1][0] <= time: #Check if proces can start
                    heapq.heappush(seq, (tasks[-1][1], tasks[-1])) #Add to min_heap based on proccesing time
                    tasks.pop()
                else:
                    break
            
            if len(seq) == 0:
                time = tasks[-1][0]
            else:
                temp, cur = heapq.heappop(seq) 
                res.append(cur[2])
                time += cur[1]

        return res


