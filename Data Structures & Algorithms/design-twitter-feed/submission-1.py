class Twitter:

    def __init__(self):
        self.feed = []
        self.following = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        count = len(self.feed)-1
        res = []
        while len(res) < 10 and count >= 0:
            cur = self.feed[count]
            if cur[0] == userId or cur[0] in self.following[userId]:
                res.append(cur[1])
            
            count -= 1

        return res
             

    def follow(self, followerId: int, followeeId: int) -> None:
        cur = self.following[followerId]
        cur.add(followeeId)
        self.following[followerId] = cur
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        cur = self.following[followerId]
        cur.discard(followeeId)
        self.following[followerId] = cur
