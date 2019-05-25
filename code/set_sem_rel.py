from depth_search import *

with open('sem_classes/KIN-SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    kinship_list = [i for i in tmp]
with open('sem_classes/SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    workers_list = [i for i in tmp]
with open('sem_classes/PARAMS.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    params_list = [i for i in tmp]


def kinsoc(data):
    if data['HeadNorm'] in kinship_list:
        data['SetRel'] = 'KIN-SOC'
        return 1
    elif data['HeadNorm'] in workers_list and data['HeadForm'][3] == 's' and data['GenNorm'] in workers_list:
        data['SetRel'] = 'KIN-SOC'
        return 1
    return 0


def param(data):
    if data['HeadNorm'] in params_list:
        data['SetRel'] = 'PAR'
        return 1
    elif 'свойство' in data['HeadSem']:
        data['SetRel'] = 'PAR'
        return 1
    #
    #
    # СПОСОБ, СРЕДСТВО
    # ОЦЕНКА (МНЕНИЕ)
    return 0


def membership(data):
    return

def ob():
    #
    # ВЫПОЛНИТЬ, ИСПОЛНИТЬ, ОСУЩЕСТВИТЬ
    # ВЗЯТЬ В СВОЕ РАСПОРЯЖЕНИЕ
    # УБИТЬ, ЛИШИТЬ ЖИЗНИ
    #
    #
    #
    #
    #
    # ИЗМЕНИТЬ СОСТОЯНИЕ
    # ОХРАНЯТЬ
    # создатель, , изменить, сделать иным, контроль, прекратить, положить конец
    return
def sag():
    #
    # обращение, высказывание
    # ГОЛОС (СОВОКУПНОСТЬ ЗВКОВ)
    # перестать, прекратить (что-то делать)
    # влиять, воздействовать
    # УДАЛИТЬ, ИСКЛЮЧИТЬ
    # ИЗМЕНИТЬ, СДЕЛАТЬ ИНЫМ
    # ДВИЖЕНИЕ, ПЕРЕМЕЩЕНИЕ
    #
    # КАСАТЬСЯ, ДОТРАГИВАТЬСЯ
    # приничениТЬ БОЛЬ

    return



