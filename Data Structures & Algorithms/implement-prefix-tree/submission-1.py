class PrefixTree:

    def __init__(self):
        self.tire = {}        

    def insert(self, word: str) -> None:
        self.tire[word] = word

    def search(self, word: str) -> bool:
        if word in self.tire:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        for i, r in self.tire.items():
            if r.startswith(prefix):
                return True
        return False
        
        