import re


def clean(x):

    lines = []

    with open(x, 'r', encoding='utf-8') as f:
        regex = '^\d+ '
        for line in f.readlines():
            try:
                num = re.match(regex, line)
                digit = re.split(' ', num[0])[0] + '\t'
                newline = re.sub(num[0], digit, line)
                newline = re.sub(' \.', '.', newline)
                newline = re.sub(' \?', '?', newline)
                newline = re.sub(' \,', ',', newline)
                newline = re.sub(' \!', '!', newline)
                newline = re.sub(' \:', ':', newline)
                newline = re.sub(' \( ', ' (', newline)
                newline = re.sub(' \)', ')', newline)
                newline = re.sub(' \%', '%', newline)
                quote = re.search('\" ([\w\d]+) \"', newline)
                if quote:
                    newline = re.sub(quote[0], '\"'+quote.group(1)+'\"', newline)
                lines.append(newline)
            except:
                return lines
        return lines

"""
path = "C:/Users/qwe/Documents/HSE/Coursework/data/temp_table.txt"
lines = clean(path)
print(lines)
with open('data/data1.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line)
"""
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
           # print(line)
        except:
            print(line)
            #continue
with open('ruteztmptmp.txt',
          'w', encoding='utf-8') as f:
    print(data)
    f.write(''.join(data))

