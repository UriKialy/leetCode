
class Solution:

    @staticmethod
    def wordBreak( s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)] == w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

    # print(wordBreak("leetcode",["leet","code"])) #True
    # print(wordBreak("applepenapple",["apple","pen"])) #True
    # print(wordBreak("catsandog",["cats","dog","sand","and","cat"])) #False

    @staticmethod
    def maximumNumber( num: str, change: list[int]) -> str:
        for i in range(len(num)):
            num_at_i=int(num[i])
            if num_at_i<change[num_at_i]:
                num=num.replace(num[i],str(change[num_at_i]),1)
        return num

    #print(maximumNumber("132",[9,8,5,0,3,6,4,2,6,8])) #832

    @staticmethod
    def kthLargestNumber( nums: list[str], k: int) -> str:
        int_list = sorted([int(s) for s in nums])
        return str(int_list[-k])
