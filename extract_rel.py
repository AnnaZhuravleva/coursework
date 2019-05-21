from depth_search import *

a = get_subc([['близкий родственник'], ['родственник']], rels_list)
b = [item for innerlist in a for item in innerlist]
tmp = []
# with open('sem_classes/KIN-SOC.txt', 'r', encoding= 'utf-8') as f:
#    tmp = f.read().split('\n')
for i in range(len(b)):
    if b[i] not in tmp:
        tmp.append(b[i])
#tmp.sort()
with open('sem_classes/KIN-SOCtmp.txt', 'w', encoding= 'utf-8') as f:
    f.write('\n'.join(sorted(tmp)))