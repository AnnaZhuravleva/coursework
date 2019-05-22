import csv

rels_list = []
with open("sem_classes/my_relations_with_concepts.csv", newline='', encoding='utf8') as rels:
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

