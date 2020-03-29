class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        arr = []
        for char in s:
            if char not in map:
                arr.append(char)
            elif len(arr) and arr.pop() == map[char]:
                continue
            else:
                return False
        return len(arr) == 0

if __name__ == "__main__":
    # result = Solution().isValid('()')
    result = Solution().isValid('(())')

    print(result)
