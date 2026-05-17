class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = [chr(c) for c in range(ord('A'), ord('Z')+1)] + \
                [chr(c) for c in range(ord('a'), ord('z')+1)] + \
                [str(i) for i in range(10)]

        take = []
        s = s.lower()
        split_a = ''.join(s.split())

        for i in split_a:
            print(i)
            if i in valid:
                take.append(i)        

        print(take)
        letters = ''.join(take)
        flip = letters[::-1]
        print(letters)
        print(flip)
        if letters == flip:
            return True
        else:
            return False