from depth_search import *

with open('sem_classes/KIN-SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    kinship_list = [i for i in tmp]
with open('sem_classes/SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    workers_list = [i for i in tmp]

def kinsoc(data):
    a = get_supc2([[data['HeadNorm']]], rels_list, max_depth=3)
    b = get_supc2([[data['GenNorm']]], rels_list, max_depth=3)
    data['HeadSem'] = sorted(list(set([item for inner in a for item in inner if item not in a])))
    data['GenSem'] = sorted(list(set([item for inner in b for item in inner if item not in b])))
    if data['HeadNorm'] in kinship_list:
        data['SetRel'] = 'KIN-SOC'
        return 1
    elif data['HeadNorm'] in workers_list and data['HeadForm'][3] == 's' and data['GenNorm'] in workers_list:
        data['SetRel'] = 'KIN-SOC'
        return 0
