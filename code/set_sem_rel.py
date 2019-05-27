"""
with open('sem_classes/KIN-SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    kinship_list = [i for i in tmp]
with open('sem_classes/SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    workers_list = [i for i in tmp]
with open('sem_classes/PARAMS.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    params_list = [i for i in tmp]
"""


def insct(a, b):
    for i in a:
        if i in b:
            return 1
    return 0


def kinsoc(data):
    kinshiplist = ['противосотящая сторона', 'соучастник', 'товарищ по работе, деятельности',
                   'преемник', 'последователь', 'родственник', 'соучастник', 'представитель интересов',
                   'заместитель должностного лица', 'представитель', 'приятель', 'друг', 'товарищ']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    if len(set(a).intersection(kinshiplist)) > 0 and len(data['HeadForm']) == 6 and data['HeadForm'][3] == 's' \
            and len(data['GenForm']) == 6 and data['HeadForm'][5] == 'y':
        data['SetRel'] = 'KIN-SOC'
        return 1
    elif data['HeadNorm'] in workers_list and len(data['HeadForm']) == 6 and data['HeadForm'][3] == 's' \
            and data['GenNorm'] in workers_list:
        data['SetRel'] = 'KIN-SOC'
        return 1
    return 0


def member(data):
    members = ['работник', 'руководитель', 'должностное лицо', 'глава', 'директор', 'творческий работник', 'член',
               'участник', 'единомышленник', 'сторонник', 'служащий', 'государственный деятель', 'лидер']
    groups = ['группа', 'совокупность людей', 'страна', 'государственная организация', 'организация', 'коллектив',
              'общество, объединение','субъект права', 'структурное подразделение','орган государственной власти',
              'административно-территориальная единица государства', 'учебное заведение','группа людей',
              'организация, учреждение', 'составная часть']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'y' and data['HeadForm'][3] == 's' and\
            len(set(a).intersection(members)) > 0 and len(data['GenForm']) == 6 \
            and data['GenForm'][5] == 'n':
        return 2
    elif len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'y' and data['HeadForm'][3] == 's' and \
            len(data['GenForm']) == 6 and data['GenForm'][5] == 'y' and data['GenForm'][3] == 'p':
        return 2
    return 0


def param(data):
    params = ['вариант, разновидность', 'физическое свойство', 'способ, средство', 'оценка (мнение)',
              'особенность', 'неодинаковость', 'свойство, характеристика']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if len(set(b).intersection(params)) > 0:
        return 3
    return 0


def ob(data):
    objs = ['выполнять, исполнить, осуществить', 'взять в свое распоряжение', 'убить, лишить жизни',
            'получить в распоряжение', 'добыча', 'извлечь, достать', 'переместить', 'назвать (произнести)',
            'уничтожить, прекратить существование', 'портить', 'вызвать мысль, чувство', 'изменить, сделать иным',
            'изменить состояние', 'притеснять', 'охранять', 'создатель', 'контроль', 'прекратить', 'положить конец',
            'организация']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if insct(a, objs) > 0:
        return 4
    return 0


def sob(data):
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    subjects = ['субъект деятельности', 'исполнитель']
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'y' and data['HeadDer'] == 'Vt' and\
            len(set(a).intersection(subjects)) > 0 and len(data['GenForm']) == 6 \
            and data['GenForm'][5] == 'n' :
        return 9
    return 0


def sag(data):
    sagents = ['обращение, высказывание', 'голос (совокупность звуков)', 'перестать, прекратить (что-то делать)',
               'влиять, воздействовать', 'удалить, исключить', 'изменить, сделать иным', 'движение, перемещение',
               'решение (заключение, вывод)', 'сохранить состояние', 'касаться, дотрагиваться', 'причинить боль',
               'целенаправленное действие', 'перемещение']
    # ФИНАНСОВЫЕ РЕЗУЛЬТАТЫ
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'n' and data['HeadDer'] == 'Vn' \
            and len(data['GenForm']) == 6 and data['GenForm'][5] == 'y':
        return 5
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'n' and data['HeadDer'] == 'Vn' \
            and len(data['GenForm']) == 6 and data['GenForm'][5] == 'y' and insct(a, sagents) > 0:
        return 5
    return 0


def wh(data):
    parts = ['вещь', 'часть', 'объект', 'отдел', 'отдел организации, учреждения',
             'структурное подразделение']
    owners = ['организация', 'группа', 'вещь', 'предмет', 'место', 'здание']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'n' \
            and len(data['GenForm']) == 6 and data['GenForm'][5] == 'n' and insct(a, parts) > 0:
        return 7
    return 0


def pos(data):
    things = ['вещь', 'предмет', 'транспорт', 'объект', 'собственность', 'техническое устройство', 'кресло', 'место']
    owners = ['организация', 'группа', 'человек', 'субъект деятельности']
    a = [i.strip('()\"\[\]\'') for i in data['HeadSem'].split('\', \'')]
    b = [i.strip('()\"\[\]\'') for i in data['GenSem'].split('\', \'')]
    if len(data['HeadForm']) == 6 and data['HeadForm'][5] == 'n' and insct(a, things) > 0: #\
            # and len(data['GenForm']) == 6 and (data['GenForm'][5] == 'y' :
        return 6
    return 0
