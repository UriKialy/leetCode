from collections import Counter


class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        rs, mag = {}, {}
        for c in ransomNote:
            rs[c] = rs.get(c, 0) + 1
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        for c in ransomNote:
            if c not in mag:
                return False
            else:
                if mag[c] < 1:
                    return False
                else:
                    mag[c] -= 1
                    rs[c] -= 1
        return all(v == 0 for v in rs.values())

    # print(canConstruct(ransomNote="aa", magazine="aab"))  # True
    # print(canConstruct(ransomNote="a", magazine="b"))  # False

    @staticmethod
    def smallestChair(times: list[list[int]], targetFriend: int) -> int:
        if targetFriend > len(times):
            return -1
        chairs = {i: [] for i in range(len(times))}  # to indicate non-vacant chairs times
        sorted_times = {i: v for i, v in enumerate(sorted(times, key=lambda x: x[0]))}
        i = 0
        for friend, (arrive, leave) in sorted_times.items():
            if not chairs[i]:
                chairs[i] = [arrive, leave]
                i += 1
            else:
                if arrive > chairs[-1]:
                    chairs[i].append(arrive)
                    chairs[i].append(leave)
                    i += 1

    @staticmethod
    def nextBeautifulNumber(n: int) -> int:
        n+=1
        while n < float('inf'):
            digit_count = Counter(str(n))
            digit_count = {int(k): v for k, v in digit_count.items()}
            for key, val in digit_count.items():
                if key != val:
                    n += 1
                    break
            else:
                return n
    print(nextBeautifulNumber(1000)) #should be 1333
