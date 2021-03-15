class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 2:
            return '11'
        elif n == 1:
            return '1'
        return self.say(self.countAndSay(n - 1))
    def say(self, n: str):
        result = ''
        t = ''
        for i in n:
            if not t:
                t = i
            elif t[-1] == i:
                t += i
            else:
                result += str(len(t)) + t[-1]
                t = i
        result += str(len(t)) + t[-1]
        return result

            