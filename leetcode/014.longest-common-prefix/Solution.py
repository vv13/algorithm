from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_nums = len(strs)
        strs.sort(key=lambda a: len(a))
        if not str_nums or ('' in strs):
            return ''
        elif str_nums == 1:
            return strs[0]
        strs_first = strs[0]
        offset = 0
        while offset < len(strs_first):
            for o in strs[1:]:
                if strs_first[offset] != o[offset]:
                    return strs_first[0:offset]
            offset += 1
        return strs_first
