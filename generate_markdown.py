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
        info['difficulty'] = information_data.get('difficulty', '')
        information_file.close()

    if os.path.exists(source_dir + 'data.json'):
        data_file = open(source_dir + '/data.json', 'r')
        information_data = json.load(data_file)
        info['tags'] = ', '.join(information_data.get('tags', []))
        info['mark'] = information_data.get('mark', '')
        rank = information_data.get('rank', '')
        info['rank'] = str(rank) + '%' if rank else ''
        data_file.close()

    links = []
    if os.path.exists(source_dir + '/Solution.py'):
        links.append('[Python]({0})'.format(os.path.join(source_dir + '/Solution.py')))
    if os.path.exists(source_dir + '/Solution.java'):
        links.append('[Java]({0})'.format(os.path.join(source_dir + '/Solution.java')))
    info['links'] = '  '.join(links)

    return '|{number}|{link_name}|{difficulty}|{tags}|{links}|{mark}|{rank}|'.format(**info)


file = open('README.md', 'w')
leetcodes = [genLineStr(i) for i in sorted(
    os.listdir('./leetcode')) if i not in ['utility', '.idea', 'leetcode.iml', 'out']]
t = string.Template(open('./README_TEMPLATE.md', 'r').read())
data = {'leetcode': os.linesep.join(leetcodes)}
file.write(t.safe_substitute({'leetcode': os.linesep.join(leetcodes)}))
file.close()
