import re, string, csv

def sorted_relation_list():
    rows = []
    with open('C:/Users/qwe/Documents/HSE/Coursework/code/sem_classes/my_relations_with_concepts.csv', newline='') as f:
        reader = csv.reader(f)
        for r in reader:
            if r not in rows:
                rows.append(r)
        rows = sorted(rows[1:])
    with open('C:/Users/qwe/Documents/HSE/Coursework/code/sem_classes/my_relations.csv', "w", newline='') as f:
        header = ['from	to	relation']
        writer = csv.writer(f, delimiter=',')
        writer.writerow(header)
        for i in range(len(rows)):
            writer.writerow(rows[i])


def format_second():
    data = []
    with open('ruteztmp.txt',
              'r', encoding='utf-8') as f:
        r = f.readlines()
        data.append(r[0])
        for line in r[1:]:
            try:
                q = line.split('	')[2]
                if q == 'ВЫШЕ\n' or q == 'ЦЕЛОЕ\n':
                    data.append(line)
            except:
                print(line)
    with open('ruteztmptmp.txt',
              'a', encoding='utf-8') as f:
        print(data)
        f.write(''.join(data))

def small(line, categories):
    new = []
    newup = []
    for cat in str(categories).split('; '):
        tmp = line.split(' ')[0] + ' '
        if tmp == tmp == 'ВЫШЕ ':
            down = cat.upper() + '	' + re.split(tmp, line)[1].split('\n')[0] + '	' + re.split(' ', tmp)[0] + '\n'
            new.append(down)
    up = re.split(tmp, line)[1].split('\n')[0] + '	' + str(categories).split('; ')[0].upper() + '	'
    if tmp == 'ВЫШЕ ':
        tmp = 'НИЖЕ'
        up += tmp + '\n'
        newup.append(up)
    elif tmp == 'НИЖЕ ':
        tmp = 'ВЫШЕ'
        up += tmp + '\n'
        newup.append(up)
    return new, newup


def format_first():
    with open('rutez.txt', 'r', encoding='utf-8') as f:
        categories = input('Ведите категорию: ').upper()
        for line in f.readlines():
            tmp = line.split(' ')[0] + ' '
            line = re.sub(r" \((.*)\)", "", line)
            #bigline = line.split(tmp)[1]
            r = small(line, categories)
            with open('ruteztmp.txt', 'a', encoding='utf-8') as f:
                f.write(''.join(r[0]))
                f.write(''.join(r[1]))


def new_format_first():
    with open('rutez.txt', 'r', encoding='utf-8') as f:
        r = []
        file = f.readlines()
        head = file[0].strip('\n')
        synonyms = file[1].split(', ')
        synonyms = [s.strip('\n\(\)') for s in synonyms]
        for line in file[2:]:
            tmp = line.split(' ')[0]
            line = line.split(str(tmp + ' '))[1]
            if tmp == 'ВЫШЕ':
                r.append('	'.join([head, line.strip('\n'), tmp]))
                for s in synonyms:
                    r.append('	'.join([s, line.strip('\n'), tmp]))
            if tmp == 'НИЖЕ':
                r.append('	'.join([line.strip('\n'), head, 'ВЫШЕ']))
    with open('ruteztmp.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(r))
        f.write('\n')
    return


while True:
    a = int(input('continue? \n1: new article\n2: format\n3: sort\n4: exit\n'))
    if a == 1:
        new_format_first()
    elif a == 2:
        format_second()
    elif a == 3:
        sorted_relation_list()
    elif a == 4:
        break
