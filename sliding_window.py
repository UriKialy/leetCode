from collections import Counter


class Solution:
    @staticmethod
    def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or not s2 and s1:
            return False
        if not s1 and s2:
            return True
        duplicate = ''
        left = right = 0
        while right < len(s2):
            if s2[right] in s1:
                duplicate += s2[right]
                print("duplicate is:", duplicate, "left is:", s2[left], "right is:", s2[right])
                if sorted(s1) == sorted(duplicate):
                    return True
                right += 1
            else:
                left += 1
                right = left
                duplicate = ''
        return False

    print(checkInclusion("adc","dcda"))
  #  print(checkInclusion("ab", "eidbaooo"))
