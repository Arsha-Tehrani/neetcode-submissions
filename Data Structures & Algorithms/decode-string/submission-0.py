class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        
        def brack(amount, start):
            nonlocal res
            cur = start
            
            # FIXED: Loop `amount` times to repeat the block
            for _ in range(amount):
                cur = start  # Reset pointer to the start of the block for each repetition
                while cur < len(s) and s[cur] != "]":
                    if s[cur].isdigit():
                        # FIXED: Replaced single-digit `int(s[cur])` with a loop 
                        # to properly support multi-digit numbers (e.g., 10, 100)
                        num = 0
                        temp = cur
                        while temp < len(s) and s[temp].isdigit():
                            num = num * 10 + int(s[temp])
                            temp += 1
                        
                        # temp is now at '[', so the inner block starts at temp + 1
                        cur = brack(num, temp + 1)
                    else:
                        res += s[cur]
                        cur += 1
            
            # FIXED: Moved `return cur + 1` OUTSIDE the `for` loop. 
            # In your original code, it was inside the loop, causing it to return on the very first iteration.
            return cur + 1  # Returns the index right after the closing ']'

        i = 0
        while i < len(s):
            if s[i].isdigit():
                # FIXED: Also added multi-digit parsing for top-level numbers
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i += 1  # Skip the '[' character
                i = brack(num, i)
            else:
                res += s[i]
                i += 1

        return res