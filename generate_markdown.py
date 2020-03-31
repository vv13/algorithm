import os
import json
import string

LEETCODE_URL = 'https://leetcode.com/problems/'


def genLineStr(s: str):
    source_dir = './leetcode/%s/' % s
    number, name, difficulty = s.split('.')
    info = {'mark': '', 'tags': '', 'number': number,
            'difficulty': difficulty, 'name': name}
    info['link_name'] = '[{0}]({1})'.format(name, source_dir)
    info['links'] = '  '.join([
        '[答案]({0})'.format(source_dir + '/solution.py'),
        '[原题]({0})'.format(LEETCODE_URL + name)])
    if os.path.exists(source_dir + 'relation.json'):
        relation_file = open(source_dir + '/relation.json', 'r')
        relation_data = json.load(relation_file)
        info['tags'] = ', '.join(relation_data.get('tags', []))
        info['mark'] = relation_data.get('mark', '')
        relation_file.close()

    return '|{number}|{link_name}|{difficulty}|{tags}|{links}|{mark}|'.format(**info)


file = open('README.md', 'w')
leetcodes = [genLineStr(i) for i in sorted(
    os.listdir('./leetcode')) if i != 'utility']
t = string.Template(open('./README_TEMPLATE.md', 'r').read())
data = {'leetcode': os.linesep.join(leetcodes)}
file.write(t.safe_substitute({'leetcode': os.linesep.join(leetcodes)}))
file.close()
