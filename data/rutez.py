import re, string


def small(line, categories):
    new = []
    newup = []
    for cat in str(categories).split(', '):
        tmp = line.split(' ')[0] + ' '
      #    line = re.sub("ЫЙ", "ОСТЬ", line)
        down = cat.upper() + '	' + \
               re.split(tmp, line)[1].split('\n')[0] + '	' + re.split(' ', tmp)[0] + '\n'
        new.append(down)
        up = re.split(tmp, line)[1].split('\n')[0] + '	' + cat.upper() + '	'
        if tmp == 'ВЫШЕ ':
            tmp = 'НИЖЕ'
        elif tmp == 'НИЖЕ ':
            tmp = 'ВЫШЕ'
        elif tmp == 'АССОЦ1 ':
            tmp = 'АССОЦ2'
        elif tmp == 'АССОЦ2 ':
            tmp = 'АССОЦ1'
        up += tmp + '\n'
        newup.append(up)
    return new, newup


with open('rutez.txt', 'r', encoding='utf-8') as f:
    categories = input('Ведите категорию: ').upper()
  #  categories = re.sub('ЫЙ', 'ОСТЬ', categories)
    for line in f.readlines():
        tmp = line.split(' ')[0] + ' '
        line = re.sub(r" \((.*)\)", "", line)
        bigline = line.split(tmp)[1]
        bigline = re.split(', ', bigline)
        bigline = [(tmp + l + '\n') for l in bigline]
        for line in bigline:
            r = small(line, categories)
            with open('ruteztmp.txt', 'a', encoding='utf-8') as f:
                f.write(''.join(r[0]))
                f.write(''.join(r[1]))


