import os
import json

LEETCODE_URL = 'https://leetcode.com/problems/'


def genLineStr(s: str):
    number, name, difficulty = s.split('.')
    source_dir = './leetcode/%s/' % s
    link_name = '[{0}]({1})'.format(name, source_dir)
    link_leetcode = '[原题]({0})'.format(LEETCODE_URL + name)
    link_answer = '[答案]({0})'.format(source_dir + '/solution.py') # TODO: find newest answer
    tags = []
    mark = ''
    if os.path.exists(source_dir + 'relation.json'):
        relation_file = open(source_dir + '/relation.json', 'r')
        relation_data = json.load(relation_file)
        tags = relation_data.get('tags', [])
        mark = relation_data.get('mark', '')
        relation_file.close()

    return '|{0}|{1}|{2}|{3}|{4}|{5}|'.format(number, link_name, difficulty, ', '.join(tags), '  '.join([link_answer, link_leetcode]), mark)


file = open('README.md', 'w')
file.write('''
## leetcode
| 序号 | 名称 | 难度 | 标签 | 链接 | 备注 |
| :----:| :---- | :----: | :----: | :----: | :---- |
''')
leetcodes = [genLineStr(i) for i in sorted(os.listdir('./leetcode')) if i != 'utility']
file.write(os.linesep.join(leetcodes))
file.close()
