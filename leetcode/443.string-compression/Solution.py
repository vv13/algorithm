from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # start index
        k = 0  # new length
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            if j - i > 1:
                chars[k] = chars[i]
                k += 1
                incr = j - i
                for i in str(j - i):
                    chars[k] = i
                    k += 1
            else:
                chars[k] = chars[i]
                k += 1
            i = j
        print(chars)
        return k
