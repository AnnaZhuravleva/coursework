from depth_search import *

with open('sem_classes/KIN-SOC.txt', 'r', encoding='utf-8') as f:
    tmp = f.read().split('\n')[1:]
    kinship_list = [i for i in tmp]

def kinsoc(data):
    if data['HeadNorm'] in kinship_list:
        data['SetRel'] = 'KIN-SOC'
        return(1)
    else:
        data['HeadSem'] = get_supc2([[data['HeadNorm']]], rels_list)
        data['GenSem'] = get_supc2([[data['GenNorm']]], rels_list)
        return(0)
