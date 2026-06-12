class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        result = float('inf')
        order = []

        def check(word1, word2):
            able = False
            done = False
            for i in range(len(word1)):
                if able == False and done == False and word1[i] != word2[i]:
                    able = True
                elif able == True and word1[i] != word2[i]:
                    able = False
                    done = True

            return able

        def bfs(word, run):
            nonlocal result
            if word == endWord:
                result = min(result, run)
                    

            for i in wordList:
                if check(word, i) and word not in visited:
                    order.append(i)

            
            visited.add(word)

        order.append(beginWord)
        run = 0
        while len(order) > 0:
            run += 1
            for x in range(len(order)):
                word = order.pop(0)
                bfs(word, run)

        if result == float('inf'):
            return 0
        return result

            