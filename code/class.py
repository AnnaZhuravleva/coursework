import csv
import pymorphy2
from depth_search import *

pmm = pymorphy2.MorphAnalyzer()
data = []
with open('C:/Users/qwe/Documents/HSE/Coursework/data/sem_classes/KIN-SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    kinship = [i for i in tmp]
    print(kinship)

with open("Data-set.csv", newline='', encoding='utf8') as f:
    reader = csv.DictReader(f, fieldnames=('№', 'Пример', 'Левый контекст', 'Вершина', '', 'Зависимое',
                                           'Правый контекст', 'Зависимые вершины', 'Зависимые генитива', 'Отношение',
                                           'Грамм. признаки вершины', 'Вершина: сем. группа',
                                           'Грам. признаки зависимого', 'Зависимое: сем. группа'))
    for row in reader:
        pair = {'Head': row['Вершина'].lower(), 'Gen': row['Зависимое'].lower(),
                'HeadNorm': pmm.normal_forms(row['Вершина'].lower())[0],
                'GenNorm': pmm.normal_forms(row['Зависимое'].lower())[0],
                'Rel': row['Отношение']}
        data.append(pair)

for i in range(12):
    if data[i]['HeadNorm'] in kinship or data[i]['GenNorm'] in kinship:
        data[i]['SetRel'] = 'KIN-SOC'
        print('!')
    else:
        data[i]['HeadSem'] = get_supc2([[data[i]['HeadNorm']]], rels_list)
        data[i]['GenSem'] = get_supc2([[data[i]['GenNorm']]], rels_list)

    print(data[i])

print(get_supc2([['руководитель']], rels_list))