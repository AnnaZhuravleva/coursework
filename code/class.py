import csv
import pymorphy2
from set_sem_rel import kinsoc, param
from depth_search import *
from extract_rel import sort_file

pmm = pymorphy2.MorphAnalyzer()


def read_file():
    data = []
    with open("data/Data-set.csv", newline='', encoding='utf8') as f:
        reader = csv.DictReader(f, fieldnames=('№', 'Пример', 'Вершина', '', 'Зависимое', 'Зависимые вершины',
                                               'Зависимые генитива', 'Отношение', 'Грамм. признаки вершины',
                                               'Грам. признаки зависимого'))
        for row in reader:
            pair = {'Head': row['Вершина'].lower(), 'Gen': row['Зависимое'].lower(),
                    'HeadNorm': pmm.normal_forms(row['Вершина'].upper())[0],
                    'GenNorm': pmm.normal_forms(row['Зависимое'].upper())[0],
                    'HeadForm': row['Грамм. признаки вершины'], 'GenForm': row['Грам. признаки зависимого'],
                    'Rel': row['Отношение'], 'HeadSem': '', 'GenSem': '', 'SetRel': ''}
            data.append(pair)
    return data


def mark_corpus(data):
    norel = []
    with open("resulttmp.csv", "w", newline='') as f:
        header = ['Вершина', 'Зависимое', 'Лемма вершины', 'Лемма зависимого', 'Форма вершины', 'Форма зависимого',
                  'Отношение', 'Гиперонимы вершины', 'Гиперонимы зависимого', 'Ярлык']
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in range(int(input("Введите количество предложений: "))):
            a = get_supc([[data[i]['HeadNorm']]], rels_list, max_depth=3)
            b = get_supc([[data[i]['GenNorm']]], rels_list, max_depth=3)
            aa = list(set([item for inner in a for item in inner]))
            bb = list(set([item for inner in b for item in inner]))
            if len(aa) > 1:
                data[i]['HeadSem'] = aa
                print("\n URA! ", aa, data[i]['Head'], "\n")
            else:
                norel.append(data[i]['HeadNorm'])
            if len(bb) > 1:
                data[i]['GenSem'] = bb
                print("\n URA! ", bb, data[i]['Gen'], "\n")
            else:
                norel.append(data[i]['GenNorm'])
            writer.writerow([data[i][key] for key in data[i]])
    with open('sem_classes/norel.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(norel))
    sort_file('sem_classes/norel.txt',)



def set_rel():
    """ if data[i]['HeadForm'][5] == 'y':
        try:
            rel = kinsoc(data[i])
        except rel == 0:
            print(data[i]['Head'],'\nnot a kinsoc\n')
        if data[i]['HeadForm'][5] == 'n':
            try:
                rel = param(data[i])
        except rel == 0:
            print(data[i]['Head'],'\nnot a param\n')"""
    return



data = read_file()
mark_corpus(data)

#if kinsoc(data[i]) == 0:
#    param(data[i])
#writer.writerow([data[i][key] for key in data[i]])
