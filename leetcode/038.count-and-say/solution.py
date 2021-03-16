class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.say(self.countAndSay(n - 1))
    def say(self, n: str):
        result = ''
        t = ''
        count = 1
        for i in n:
            if not t:
                t = i
            elif t[-1] == i:
                count += 1
            else:
                result += str(count) + t[-1]
                t = i
                count = 1
        result += str(count) + t[-1]
        return result

class Solution1:
    def countAndSay(self, n: int) -> str:
        prev = ''
        cur = '1'
        for _ in range(1, n):
            prev = cur
            cur = ''
            start = 0
            end = 0
            while end < len(prev):
                while end < len(prev) and prev[start] == prev[end]:
                    end += 1
                cur += str(end - start) + prev[start]
                start = end
        return cur

print(Solution1().countAndSay(5))


            
