import os
import json
import string

LEETCODE_URL = 'https://leetcode.com/problems/'


def genLineStr(s: str):
    source_dir = './leetcode/%s/' % s
    number, name = s.split('.')
    info = {'mark': '', 'tags': '', 'rank': '', 'number': int(number),
            'difficulty': '', 'name': name}
    info['link_name'] = '[{0}]({1})'.format(name, source_dir)
    if os.path.exists(source_dir + 'information.json'):
        information_file = open(source_dir + '/information.json', 'r')
        information_data = json.load(information_file)
        info['tags'] = ', '.join(information_data.get('tags', []))
        info['mark'] = information_data.get('mark', '')
        info['difficulty'] = information_data.get('difficulty', '')
        rank = information_data.get('rank', '')
        info['rank'] = str(rank) + '%' if rank else ''
        information_file.close()

    links = [
        '[答案]({0})'.format(os.path.join(source_dir + '/solution.py'))
    ]
    if os.path.exists(source_dir + 'DRAFT.md'):
        links.append('[解题思路]({0})'.format(source_dir + '/DRAFT.md'))
    info['links'] = '  '.join(links)

    return '|{number}|{link_name}|{difficulty}|{tags}|{links}|{mark}|{rank}|'.format(**info)


file = open('README.md', 'w')
leetcodes = [genLineStr(i) for i in sorted(
    os.listdir('./leetcode')) if i != 'utility']
t = string.Template(open('./README_TEMPLATE.md', 'r').read())
data = {'leetcode': os.linesep.join(leetcodes)}
file.write(t.safe_substitute({'leetcode': os.linesep.join(leetcodes)}))
file.close()
