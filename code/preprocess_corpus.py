import csv
import pymorphy2
import gensim


pmm = pymorphy2.MorphAnalyzer()
rels_list = []
m = 'ruscorpora_mystem_cbow_300_2_2015.bin.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)
model.init_sims(replace=True)
with open("sem_classes/my_relations_with_concepts.csv", newline='') as rels:
    reader = csv.DictReader(rels, delimiter="\t")
    for row in reader:
        rels_list.append(row)


def sort_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        p = [m.lower() for m in f.read().split('\n')]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(set(p))))


def get_supc(concept_list, rels_list, has_up=True, depth=0, max_depth=-1):
    if (not has_up) or depth >= max_depth > 0:
        return concept_list
    has_up = False
    new_list = []
    for word in concept_list[-1]:
        for row in rels_list:
            if row['from'].lower() == word.lower() and row['relation'] == 'ВЫШЕ':
                if all(row['to'].lower() not in hypo for hypo in concept_list):
                    new_list.append(row['to'].lower())
                    has_up = True
    if has_up:
        concept_list.append(new_list)
    return get_supc(concept_list, rels_list, has_up, depth + 1, max_depth)


def read_blank_file():
    data = []
    with open("data/Data-set.csv", newline='', encoding='utf8') as f:
        reader = csv.DictReader(f, fieldnames=('№', 'Пример', 'Вершина', 'Зависимое', 'Отношение',
                                               'Грамм. признаки вершины', 'Грам. признаки зависимого',
                                               'Производящее вершины', 'Производящее зависимого'))
        for row in reader:
            pair = {'№': row['№'], 'Head': row['Вершина'].lower(), 'Gen': row['Зависимое'].lower(),
                    'HeadNorm': pmm.normal_forms(row['Вершина'].strip('"').upper())[0],
                    'GenNorm': pmm.normal_forms(row['Зависимое'].strip('"').upper())[0],
                    'HeadForm': row['Грамм. признаки вершины'], 'GenForm': row['Грам. признаки зависимого'],
                    'HeadDer': row['Производящее вершины'], 'GenDer': row['Производящее зависимого'],
                    'Rel': row['Отношение']}
            data.append(pair)
    data = data[1:]
    with open("data/Data-set_normalized.csv", "w", newline='', encoding='utf8') as f:
        h = ['№', 'Head', 'Gen', 'HeadNorm', 'GenNorm', 'HeadForm', 'GenForm',  'HeadDer', 'GenDer', 'Rel']
        writer = csv.writer(f, delimiter=',')
        writer.writerow(h)
        for i in range(len(data)):
            writer.writerow([data[i][key] for key in data[i]])
    return


def read_file_with_norm_forms():
    data = []
    with open("data/Data-set_normalized.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=('№', 'Head', 'Gen', 'HeadNorm', 'GenNorm', 'HeadForm', 'GenForm', 'Rel',
                                               'HeadSem', 'GenSem', 'SetRel', 'HeadDer', 'GenDer'))
        for row in reader:
            pair = {'№': row['№'], 'Head': row['Head'], 'Gen': row['Gen'].lower(), 'HeadNorm': row['HeadNorm'],
                    'GenNorm': row['GenNorm'], 'HeadForm': row['HeadForm'], 'GenForm': row['GenForm'],
                    'HeadDer': row['HeadDer'], 'GenDer': row['GenDer'], 'Rel': row['Rel'],
                    'HeadSem': '', 'GenSem': '', 'HeadSemVW': '', 'GenSemVW': '', 'SetRel': '', 'SetRelWV': ''}
            data.append(pair)
    return data


def vw(word):
    cats = ['родственник', 'свойство', 'деятель', 'действие', 'качество', 'должность',
            'организация', 'предмет', 'человек', 'глава', 'руководитель', 'коллектив'
            'учреждение', 'группа', 'часть', 'отдел', 'документ', 'устройство',
            'двигаться', 'перемещаться']
    rel_dict = {}
    for cat in cats:
        try:
            rel_dict[cat] = model.similarity(cat + '_S', word + '_S')
        except:
            rel_dict[cat] = 0
    return max(rel_dict, key=rel_dict.get)


def mark_corpus(data):
    norel = []
    with open("result.csv", "w", newline='', encoding='utf-8') as f:
        header = ['№', 'Вершина', 'Зависимое', 'Лемма вершины', 'Лемма зависимого', 'Форма вершины', 'Форма зависимого',
                  'Производящее вершины', 'Производящее зависимого',
                  'Отношение', 'Гиперонимы вершины', 'Гиперонимы зависимого',
                  'Гиперонимы вершины WV', 'Гиперонимы зависимого WV', 'Ярлык']
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in range(1, int(input("Enter number of sentences no more than length of your Data-set: "))):
            a = get_supc([[data[i]['HeadNorm']]], rels_list, max_depth=3)
            b = get_supc([[data[i]['GenNorm']]], rels_list, max_depth=3)
            aa = list(set([item for inner in a for item in inner]))
            bb = list(set([item for inner in b for item in inner]))
            if len(aa) > 0:
                data[i]['HeadSem'] = aa
            elif len(data[i]['HeadForm']) == 6 and data[i]['HeadForm'][1] == 'p' and data[i]['HeadForm'][5] == 'y':
                data[i]['HeadSem'] = ['человек', 'субъект деятельности', 'имя']
            else:
                norel.append(data[i]['HeadNorm'])
            if len(bb) > 0:
                data[i]['GenSem'] = bb
            elif len(data[i]['GenForm']) == 6 and data[i]['GenForm'][1] == 'p' and data[i]['GenForm'][5] == 'y':
                data[i]['GenSem'] = ['человек', 'субъект деятельности', 'имя']
            else:
                norel.append(data[i]['GenNorm'])
            data[i]['HeadSemVW'] = vw(data[i]['HeadNorm'])
            data[i]['GenSemVW'] = vw(data[i]['GenNorm'])
            writer.writerow([data[i][key] for key in data[i]])
    with open('sem_classes/norel.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(norel))
    sort_file('sem_classes/norel.txt',)
    return
