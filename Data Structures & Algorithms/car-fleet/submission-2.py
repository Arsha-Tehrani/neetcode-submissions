class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        n = len(position)
        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        stack.append(cars[0])
        for i in range(len(cars)):
            time_taken = (target - cars[i][0]) / cars[i][1]
            time_taken_b = (target - stack[0][0]) / stack[0][1]
            if time_taken > time_taken_b:
                res += 1
                stack.clear()
                stack.append(cars[i])

        return res

