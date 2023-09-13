# _*_ condign:utf-8

import glob
import json

datas = glob.glob("E:/project/python/chinese-poetry/全唐诗/poet.*.json")

for data in datas:
    with open(data, 'r', encoding='utf-8') as fp:
        item = json.load(fp)
        for each in item :
            if len(each['paragraphs']) == 2 and len(each['paragraphs'][0]) == 12 and len(each['paragraphs'][1]) == 12:
                with open("input.txt", "a", encoding='utf-8') as f:
                    f.write("".join(each['paragraphs']))
                    f.write('\n')

