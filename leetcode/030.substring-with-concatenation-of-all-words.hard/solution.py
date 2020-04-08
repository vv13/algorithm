from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_len = len(words[0])
        sub_len = word_len * len(words)
        result = []

        word_cnt = {}
        for w in words:
            word_cnt[w] = 1 if w not in word_cnt else word_cnt[w] + 1

        for i in range(0, len(s) - sub_len + 1):
            sub = s[i:i + sub_len]
            sub_cnt = {}
            for j in range(0, len(sub), word_len):
                w = sub[j:j + word_len]
                sub_cnt[w] = 1 if w not in sub_cnt else sub_cnt[w] + 1
                if (w not in word_cnt) or (sub_cnt[w] > word_cnt[w]):
                    j = -1
                    break
            if j == len(sub) - word_len:
                result.append(i)

        return result
