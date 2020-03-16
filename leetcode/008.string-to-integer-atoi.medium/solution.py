class Solution:
    def myAtoi(self, str: str) -> int:
        MAX_NUM = pow(2, 31) - 1
        # discard whitespace
        str = str.strip()
        # check if can convert to int
        if not str or (not str[0].isnumeric() and str[0] not in ['-', '+']):
            return 0

        ret = ''
        index = 0
        signal = 1
        # set sigm
        if str[0] == '-':
            index += 1
            signal = -1
        elif str[0] == '+':
            index += 1

        while index < len(str):
            if not str[index].isnumeric():
                break
            ret += str[index]
            index += 1
            if int(ret) > MAX_NUM:
                return MAX_NUM if signal == 1 else -MAX_NUM - 1

        return int(ret) * signal if ret else 0
