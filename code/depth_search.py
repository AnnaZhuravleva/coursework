import csv

rels_list = []
with open("sem_classes/my_relations_with_concepts.csv", newline='') as rels:
    reader = csv.DictReader(rels, delimiter="\t")
    for row in reader:
        rels_list.append(row)


def get_supc2(concept_list, rels_list, has_up=True, depth=0, max_depth=-1):
    """
    Get list of all hypernym chains of the query
    - up a level
    - add all 'выше' concepts to list
    [[level_1, level_2.1, level_3.1], [level_1, level_2.2, level_3.2], etc...]
    :param concept_list: search input
    :param rels_list: imported set of relations
    :param max_depth: maximum allowed number of hypernyms
    :param has_up: (internal) bool(current top concept has a superconcept)
    :param depth: (internal) current depth in the ontology
    :return: list of superconcept for every meaning of query
    """
    new_cl = concept_list[:]
    if (not has_up) or depth >= max_depth > 0:
        return new_cl
    has_up = False
    for chain in concept_list:
        index = new_cl.index(chain)
        word = chain[-1]
        for row in rels_list:
            new_chain = chain[:]
            if row['from'].lower() == word.lower() and row['relation'] == 'ВЫШЕ':
                new_chain.append(row['to'].lower())
                new_cl.insert(index + 1, new_chain)
                has_up = True
        if has_up:
            new_cl.remove(chain)
    return get_supc2(new_cl, rels_list, has_up, depth+1, max_depth)


def get_supc(concept_list, rels_list, has_up=True, depth=0, max_depth=-1):
    """
    Find list of all hypernyms of query by level down
    [[level_1], [level_2.1, level_2.2], [level_3.1, level_3.2, level_3.3], etc...]
    :param concept_list: search input
    :param rels_list: imported set of relations
    :param max_depth: maximum allowed number of hyponyms
    :param has_up: (internal) bool(current top concept has a subconcept)
    :param depth: (internal) current depth in the ontology
    :return: list of subconcepts for every meaning of query
    """
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


def get_subc2(concept_list, rels_list, has_down=True, depth=0, max_depth=-1):
    """
    Get list of all hyponym chains for word in query
    - down a level
    - add all 'ниже' concepts to list
    [[level_1, level_2.1, level_3.1], [level_1, level_2.2, level_3.2], etc...]
    :param concept_list: search input
    :param rels_list: imported set of relations
    :param max_depth: maximum allowed number of hyponyms
    :param has_down: (internal) bool(current top concept has a subconcept)
    :param depth: (internal) current depth in the ontology
    :return: list of subconcepts for every meaning of query
    """
    new_cl = concept_list[:]
    if (not has_down) or depth >= max_depth > 0:
        return new_cl
    for chain in concept_list:
        has_down = False
        index = new_cl.index(chain)
        word = chain[-1]
        for row in rels_list:
            new_chain = chain[:]
            if row['from'].lower() == word.lower() and row['relation'] == 'НИЖЕ':
                new_chain.append(row['to'].lower())
                new_cl.insert(index + 1, new_chain)
                has_down = True
        if has_down:
            new_cl.remove(chain)
    return get_subc2(new_cl, rels_list, has_down, depth+1, max_depth)


def get_subc(concept_list, rels_list, has_down=True, depth=0, max_depth=-1):
    """
    Find list of all hyponyms of query by level down
    [[level_1], [level_2.1, level_2.2], [level_3.1, level_3.2, level_3.3], etc...]
    :param concept_list: search input
    :param rels_list: imported set of relations
    :param max_depth: maximum allowed number of hyponyms
    :param has_down: (internal) bool(current top concept has a subconcept)
    :param depth: (internal) current depth in the ontology
    :return: list of subconcepts for every meaning of query
    """
    if (not has_down) or depth >= max_depth > 0:
        return concept_list
    has_down = False
    new_list = []
    for word in concept_list[-1]:
        for row in rels_list:
            if row['from'].lower() == word.lower() and row['relation'] == 'НИЖЕ':
                if all(row['to'].lower() not in hypo for hypo in concept_list):
                    new_list.append(row['to'].lower())
                    has_down = True
    if has_down:
        concept_list.append(new_list)
    return get_subc(concept_list, rels_list, has_down, depth+1, max_depth)
"""
a = get_supc([['собака'], ['кошка']], rels_list)
print(a)
"""
[['собака'], ['кошка'],
['домашнее животное', 'кошачьи'], 
['животное', 'хищное млекопитающее'], 
['живой организм', 'млекопитающее', 'дикое животное', 'хищное животное'], 
['биологическая сущность', 'позвоночное животное'], 
['физическая сущность'], 
['постоянная сущность']]
"""

a = get_supc2([['собака'], ["кошка"]], rels_list)
print(a)
"""
[['собака', 'домашнее животное', 'животное', 'живой организм', 'биологическая сущность', 'физическая сущность', 'постоянная сущность'], 
['собака', 'млекопитающее', 'позвоночное животное', 'животное', 'живой организм', 'биологическая сущность', 'физическая сущность', 'постоянная сущность'], 
['кошка', 'кошачьи', 'хищное млекопитающее', 'хищное животное', 'животное', 'живой организм', 'биологическая сущность', 'физическая сущность', 'постоянная сущность'], 
['кошка', 'кошачьи', 'хищное млекопитающее', 'дикое животное', 'животное', 'живой организм', 'биологическая сущность', 'физическая сущность', 'постоянная сущность'],
['кошка', 'кошачьи', 'хищное млекопитающее', 'млекопитающее', 'позвоночное животное', 'животное', 'живой организм', 'биологическая сущность', 'физическая сущность', 'постоянная сущность']]
"""

b = get_subc([['собака']], rels_list)
print(b)
"""
[['собака'], 
['служебная собака', 'охотничья собака', 'комнатная собака', 'пудель', 'бульдог', 'пинчер', 'щенок (собака)', 'кобель (собака)', 'беспородная собака', 'ротвейлер', 'лабрадор (порода собак)', 'чихуахуа (порода собак)'], 
['поисковая собака', 'овчарка', 'боксер (собака)', 'такса (собака)', 'волкодав', 'лайка (собака)', 'спаниель', 'терьер', 'борзая собака', 'легавая собака', 'болонка', 'доберман'], 
['немецкая овчарка', 'кокер-спаниель', 'питбультерьер', 'йоркширский терьер', 'стаффордширский терьер', 'сеттер']]
"""

c = get_subc2([['собака']], rels_list)
print(c)
"""
[['собака', 'чихуахуа (порода собак)'], 
['собака', 'лабрадор (порода собак)'], 
['собака', 'ротвейлер'], 
['собака', 'беспородная собака'],
['собака', 'кобель (собака)'], 
['собака', 'щенок (собака)'], 
['собака', 'пинчер', 'доберман'], 
['собака', 'бульдог'], 
['собака', 'пудель'], 
['собака', 'комнатная собака', 'болонка'], 
['собака', 'комнатная собака', 'пудель'], 
['собака', 'охотничья собака', 'легавая собака', 'сеттер'], 
['собака', 'охотничья собака', 'борзая собака'], 
['собака', 'охотничья собака', 'терьер', 'стаффордширский терьер'], 
['собака', 'охотничья собака', 'терьер', 'йоркширский терьер'], 
['собака', 'охотничья собака', 'терьер', 'питбультерьер'], 
['собака', 'охотничья собака', 'спаниель', 'кокер-спаниель'], 
['собака', 'охотничья собака', 'лайка (собака)'], 
['собака', 'охотничья собака', 'волкодав'], 
['собака', 'охотничья собака', 'такса (собака)'], 
['собака', 'служебная собака', 'боксер (собака)'], 
['собака', 'служебная собака', 'овчарка', 'немецкая овчарка'], 
['собака', 'служебная собака', 'поисковая собака']]
"""

# a = get_supc([['собака']], rels_list, max_depth=1)
# print(a)
#
# b = get_subc([['собака']], rels_list, max_depth=4)
# print(b)
#
# c = get_subc2([['собака']], rels_list, max_depth=2)
# print(c)
"""



