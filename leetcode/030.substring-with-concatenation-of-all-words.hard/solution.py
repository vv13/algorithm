from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        def checkIsSubstring(sub: str, words: List[str]):
            word_len = len(words[0])
                
            for word in words:
                idx = -1
                for i in range(0, len(sub), word_len):
                    if sub[i:i + word_len] == word:
                        idx = i
                if idx == -1:
                    return False
                sub = sub[0:idx] + sub[idx + word_len:]
            return True

        sub_len = len(words[0]) * len(words)
        result = []
        for i in range(0, len(s) - sub_len + 1):
            sub = s[i:i + sub_len]
            if checkIsSubstring(sub, words):
                result.append(i)
        return result
