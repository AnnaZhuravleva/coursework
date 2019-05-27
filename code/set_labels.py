import datetime
import csv
from set_sem_rel import *


rels_dict = ['None', 'KIN-SOC', 'MB', 'PAR', 'OB', 'SAG', 'POS', 'WH', 'ATR']


def read_file_with_sem_tags():
    data = []
    with open("C:/Users/qwe/Documents/HSE/Coursework/code/result.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=('№', 'Вершина', 'Зависимое', 'Лемма вершины', 'Лемма зависимого',
                                               'Форма вершины', 'Форма зависимого',
                                               'Производящее вершины', 'Производящее зависимого', 'Отношение',
                                               'Гиперонимы вершины', 'Гиперонимы зависимого',
                                               'Гиперонимы вершины WV', 'Гиперонимы зависимого WV',
                                               'Ярлык', 'Ярлык VW'))

        for row in reader:
            pair = {'№': row['№'], 'Head': row['Вершина'], 'Gen': row['Зависимое'].lower(),
                    'HeadNorm': row['Лемма вершины'], 'GenNorm': row['Лемма зависимого'],
                    'HeadForm': row['Форма вершины'], 'GenForm': row['Форма зависимого'],
                    'HeadDer': row['Производящее вершины'], 'GenDer': row['Производящее зависимого'],
                    'Rel': row['Отношение'],
                    'HeadSem': row['Гиперонимы вершины'], 'GenSem': row['Гиперонимы зависимого'],
                    'HeadSemVW': row['Гиперонимы вершины WV'], 'GenSemVW': row['Гиперонимы зависимого WV'],
                    'SetRel': '', 'SetRelWV': ''}
            data.append(pair)
    return data


def set_r(data):
    rel = 0
    try:
        rel = kinsoc(data)
    except:
        pass
    if rel == 0:
        try:
            rel = member(data)
        except:
            pass
    if rel == 0:
        try:
            rel = param(data)
        except:
            pass
    if rel == 0:
        try:
            rel = ob(data)
        except:
            pass
    if rel == 0:
        try:
            rel = pos(data)
        except:
            pass
    if rel == 0:
        rel = 8
    return rel


def set_rvw(data):
    relwv = 0
    if data['HeadSemVW'] == 'родственник':
        relwv = 1
    if data['HeadSemVW'] == 'свойство':
        relwv = 3
    if data['HeadSemVW'] == 'действие':
        relwv = 4
    if data['HeadSemVW'] == 'деятель':
        relwv = 5
    if data['HeadSemVW'] == 'предмет':
        relwv = 6
    return relwv


def set_rel(data):
    hit = 0
    hitwv = 0
    new_data = []
    for i in range(int(input('Enter number of noun-groups that you want to get semantic class of: '))):
        rel = set_r(data[i])
        relwv = set_rvw(data[i])
        print(rels_dict[rel], rels_dict[relwv], data[i]['Rel'], data[i]['Head'], data[i]['Gen'])
        new_data.append([rels_dict[rel], rels_dict[relwv], data[i]['Rel'], data[i]['Head'], data[i]['Gen']])
    for i in new_data:
        if i[0] == i[2]:
            hit += 1
        if i[1] == i[2]:
            hitwv += 1
    with open('feedback.txt', 'w', encoding='utf-8') as f:
        f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M")+'\n')
        f.write('==========================================================================\n'
                'Column   RuTez   - classification based on linguistic ontology \'RuTez\'\n'
                'Column   W2V     - classification based on model \'RusVectores\'\n'
                'Column   Initial - semantic relation from Data-set\n'
                'Column   Head    - Head Noun\n'
                'Column   Gen     - Genitive\n'
                '==========================================================================\n'
                'RuTez      W2V     Initial     Head        Gen\n'
                '---------------------------------------------------------------------------\n')
        for i in new_data:
            f.write('   '.join(i)+'\n')
        f.write('---------------------------------------------------------------------------\n')
        f.write('       '.join([str(hit/len(new_data)), str(hitwv/len(new_data))]))
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    print(hit/len(new_data), hitwv/len(new_data))
    return


