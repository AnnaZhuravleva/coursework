import csv
import pymorphy2
import string
import  re
from depth_search import *

pmm = pymorphy2.MorphAnalyzer()
"""

# with open('sem_classes/KIN-SOC.txt', 'r', encoding= 'utf-8') as f:
#    tmp = f.read().split('\n')

a = get_subc([['близкий родственник'], ['родственник']], rels_list)
b = [item for innerlist in a for item in innerlist]
tmp = []
# with open('sem_classes/KIN-SOC.txt', 'r', encoding= 'utf-8') as f:
#    tmp = f.read().split('\n')
for i in range(len(b)):
    if b[i] not in tmp:
        tmp.append(b[i])
with open('sem_classes/KIN-SOC.txt', 'w', encoding= 'utf-8') as f:
    f.write('\n'.join(sorted(tmp)))

# Extract KIN-SOC relation
a = get_subc([['государственный служащий']], rels_list)
b = [item for innerlist in a for item in innerlist]
tmp = []s
for i in range(len(b)):
    if b[i] not in tmp:
        tmp.append(b[i])
with open('sem_classes/SOC.txt', 'w', encoding= 'utf-8') as f:
   # f.write('\n'.join(sorted(tmp)))
"""


def one_relation_corpus(data):  # extract one relation from corpus
    name = str(input("Выберите отношение: {KIN-SOC, MB, WH, POS, SAG, SPA, OB, ATR, PAR}. Вы выбрали: "))
    filename = name + '.csv'
    with open(filename, "w", newline='') as f:
        header = ['Вершина', 'Зависимое', 'Лемма вершины', 'Лемма зависимого', 'Форма вершины', 'Форма зависимого',
                  'Отношение', 'Гиперонимы вершины', 'Гиперонимы зависимого', 'Ярлык']
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in range(len(data)):
            if data[i]['Rel'] == name:
                writer.writerow([data[i][key] for key in data[i]])  # If corpus doesn't have information of semantics:
                # a = get_supc2([[data[i]['HeadNorm']]], rels_list, max_depth=5)
                # b = get_supc2([[data[i]['GenNorm']]], rels_list, max_depth=5)
                # data[i]['HeadSem'] = sorted(list(set([item for inner in a for item in inner])))
                # data[i]['GenSem'] = sorted(list(set([item for inner in b for item in inner])))


def extract_hyponyms_to_file(filename, depth):
    with open(filename, 'a', encoding='utf-8') as f:
        p = get_subc([[str(input('Введите категорию: '))]], rels_list, max_depth=depth)
        aa = list(set([item for inner in p for item in inner]))
        f.write('\n'.join(aa))


def buildmycorpus():
    with open('sem_classes/tmp.txt', 'a', encoding='utf-8') as f:
        name = input('введите категорию: ')
        m = int(input('Введите глубину: '))
        b = get_subc2([[name]], rels_list, max_depth=m)
        c = get_subc([[name]], rels_list, max_depth=m)
        b = sorted(list(set([item for inner in b for item in inner])))
        c = sorted(list(set([item for inner in c for item in inner])))
        a = [b, c]
        a = sorted(list(set([item for inner in a for item in inner])))
        tmp = [(i.upper() + '	' + name.upper() + '	ВЫШЕ') for i in a]
        f.write('\n'.join(tmp))
    return


def sort_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        p = [m.lower() for m in f.read().split('\n')]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(set(p))))

# while int(input('continue? If you want - type "1", if not - type whatever you want')) == 1:
# buildmycorpus()
# extract_hyponyms_to_file(str('что ищем?: '), str(input('введите путь к файлу: ')), int(input('введите глубину: ')))

# sort_file('sem_classes/PARAMS.txt')


"""
Фwith open('sem_classes/tmp.txt', 'r', encoding='utf-8') as f:
    data = []
    for line in f.readlines():
        line = re.split('	', line)[0]
        data.append(line)
with open('sem_classes/PARAMStmp', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sorted(list(set(data)))))
"""


#extract_hyponyms_to_file('sem_classes/MBtmp.txt', 4)

sort_file('sem_classes/norel.txt')


