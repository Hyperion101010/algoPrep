class Twitter:

    def __init__(self):
      # For getnewsfeed to work
      # We need all users this user follows to be each neighbour of this user.
      # If A follows B then B is neaghbour of A. A --> B
      # So when this user follows someone we add this user in our graph.
      # When it is unfollowed as A unfollows B then A != --> B. Remove the node connection.
      # So each node connection we will use set or deque.
      # Lets keep a global counter for tweets.
      # For each user maintain a heap of the latest tweet on top.

      # Get newsfeed
      # In our heap we use 10 elements each, so for F followers we have F times iteration.
      # Now for these followers, after all iteration we do a heapify.
      # heapify is O(n) so for total n elements O(n)
      # Now to get k elements from n length list we will take O(n log k)
      # Also, here n is the total elements and O(log k) for all elements.
      # For normal heap pop and push have complexity as O(log n)

      self.counter = 0
      self.user_to_tweet_map = dict()
      self.graph = dict()

      """
        The crux of the problem is, we will use a user to tweet map to store the mapping of which user has what tweets.
        Then we will store all the user relation of following into a graph.
        So, this will allow quick follow and unfollow.

        We will only visit those graph nodes which are neighbours and also its own user tweets when searching.
        Now, in the user when we unfollow, we can remove the node by deque remove operation.

        We also ensure no duplicate follow requests are present before follow request is processed.

        For getting the most k, tweets we use heap nlargest function to return the function in constant time.
        Then we fetch 10 tweets for all users, sort it and then return the most recent 10 tweets.
      """


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.user_to_tweet_map:
            self.user_to_tweet_map[userId].append((self.counter, tweetId))
        else:
            self.user_to_tweet_map[userId] = [(self.counter, tweetId)]
        
        self.counter += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        hp = []

        if userId in self.graph:
            for each_followed in self.graph[userId]:
                if each_followed in self.user_to_tweet_map:
                    hp.extend(self.user_to_tweet_map[each_followed][-10:])

        if userId in self.user_to_tweet_map:
            hp.extend(self.user_to_tweet_map[userId][-10:])

        heapify(hp)

        tmp = heapq.nlargest(10, hp)

        ans = []

        for time, each_ele in tmp:
            ans.append(each_ele)

        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.graph:
            self.graph[followerId].add(followeeId)
        else:
            self.graph[followerId] = set()
            self.graph[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.graph and followeeId in self.graph[followerId]:
            self.graph[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
