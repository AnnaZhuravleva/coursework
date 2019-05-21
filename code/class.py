import csv
import pymorphy2
from set_sem_rel import kinsoc

pmm = pymorphy2.MorphAnalyzer()
data = []

with open("data/Data-set.csv", newline='', encoding='utf8') as f:
    reader = csv.DictReader(f, fieldnames=('№', 'Пример', 'Вершина', '', 'Зависимое', 'Зависимые вершины',
                                           'Зависимые генитива', 'Отношение', 'Грамм. признаки вершины',
                                           'Грам. признаки зависимого'))
    for row in reader:
        pair = {'Head': row['Вершина'].lower(), 'Gen': row['Зависимое'].lower(),
                'HeadNorm': pmm.normal_forms(row['Вершина'].lower())[0],
                'GenNorm': pmm.normal_forms(row['Зависимое'].lower())[0],
                'Rel': row['Отношение']}
        data.append(pair)

for i in range(2):
    print(kinsoc(data[i]))
    print(data[i])

