class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        result = 0
        order = []

        for i in tokens:
            print(order)
            if i not in operands:
                order.append(i)
            if i == '+' and order is not None:
                result = int(order[-1]) + int(order[-2])
                order.pop()
                order.pop()
                order.append(result)
            if i == '-' and order is not None:
                result = int(order[-2]) - int(order[-1])
                order.pop()
                order.pop()
                order.append(result)
            if i == '*' and order is not None:
                result = int(order[-1]) * int(order[-2])
                order.pop()
                order.pop()
                order.append(result)
            if i == '/' and order is not None:
                result = int(order[-2]) / int(order[-1])
                order.pop()
                order.pop()
                order.append(result)
        return int(order[0])