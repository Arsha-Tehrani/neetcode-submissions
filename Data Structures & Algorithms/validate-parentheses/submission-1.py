class Solution:
    def isValid(self, s: str) -> bool:
        open_que = []
        close_que = []
        opens = ['(','[','{']
        closed = [')',']','}']
        relate = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in opens:
                open_que.append(i)
            elif i in closed:
                if not open_que:
                    return False
                if open_que[-1] != relate[i]:
                    return False
                else:
                    open_que.pop()
        
        if len(open_que) > 0:
            return False
        else:
            return True