import os

LEETCODE_URL = 'https://leetcode.com/problems/'


def genLineStr(s: str):
    number, name, difficulty = s.split('.')
    link_name = '[{0}](./leetcode/{1})'.format(name, s)
    link_leetcode = '[leetcode]({0})'.format(LEETCODE_URL + name)
    return '|{0}|{1}|{2}|{3}|'.format(number, link_name, difficulty, link_leetcode)


file = open('README.md', 'w')
file.write('''
## leetcode
| index | name | difficulty | link |
| :----:| :---- | :----: | :----:
''')
leetcodes = [genLineStr(i) for i in sorted(os.listdir('./leetcode'))]
file.write(os.linesep.join(leetcodes))
file.close()
