class Solution:

    def encode(self, strs: List[str]) -> str:
         if len(strs) == 0:
            return "None"
         shift = 10
         sep = chr(255)
         joined = sep.join(strs)
         encoded = "".join(chr(ord(c) + shift) for c in joined)
         return encoded

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        shift = 10
        sep = chr(255)
        revert = "".join(chr(ord(c) - shift) for c in s)
        decoded = revert.split(sep)
        return decoded

