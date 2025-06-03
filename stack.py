import collections
import math


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if not s: return True
        if len(s) % 2 != 0 or len(set(s)) == 1:
            return False
        stack = []
        for ch in s:
            if ch in '[{(':
                stack.append(ch)
            elif ch in "]})":
                if not stack:
                    print("not enough chars")
                    return False
                else:
                    check = stack.pop()
                    if (ch == "]" and check == "[") or (ch == "}" and check == "{") or (ch == ")" and check == "("):
                        continue
                    else:
                        print("incorrect orders of chars")
                        return False
            else:
                print("invalid character")
                return False

        return len(stack) == 0

    #   print(isValid("({[]})"))
    #  print(isValid("(("))

    @staticmethod
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

    #   print(dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]

    @staticmethod
    def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        all_lists = [[x, y, (target - x) / y] for x, y in zip(position, speed)]
        all_lists=sorted(all_lists, key=lambda x: x[0], reverse=True)
        stack=[all_lists[0][2]]
        res=0
        for i in range(1,len(all_lists)-1):
            print("stack is: ",stack, " res is: ",res)
            if stack and all_lists[i][2]>=stack[-1]:
                stack.append(all_lists[i][2])
                res+=1
        return len(stack)
   # print(carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])) #3
    print(carFleet(10,[6,8],[3,2]))  #2


    





    class MinStack:

        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self) -> None:
            if self.stack:
                val = self.stack.pop()
                if val == self.min_stack[-1]:
                    self.min_stack.pop()

        def top(self) -> int:
            if self.stack:
                return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
