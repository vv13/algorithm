import os
import json

LEETCODE_URL = 'https://leetcode.com/problems/'


def genLineStr(s: str):
    number, name, difficulty = s.split('.')
    source_dir = './leetcode/%s/' % s
    link_name = '[{0}]({1})'.format(name, source_dir)
    link_leetcode = '[leetcode]({0})'.format(LEETCODE_URL + name)
    tags = []
    if os.path.exists(source_dir + 'relation.json'):
        relation_file = open(source_dir + '/relation.json', 'r')
        relation_data = json.load(relation_file)
        tags = relation_data.get('tags', [])
        relation_file.close()

    return '|{0}|{1}|{2}|{3}|{4}|'.format(number, link_name, difficulty, ', '.join(tags), link_leetcode)


file = open('README.md', 'w')
file.write('''
## leetcode
| index | name | difficulty | tags | link |
| :----:| :---- | :----: | :----: | :----:
''')
leetcodes = [genLineStr(i) for i in sorted(os.listdir('./leetcode'))]
file.write(os.linesep.join(leetcodes))
file.close()
