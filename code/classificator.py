print('You have to wait till all the components are installed...')


from preprocess_corpus import *


if __name__ == '__main__':
    while True:
        a = int(input('continue?\n'
                      '1: You have file without lemmas;\n'
                      '2: You have file with lemmas but without hyperonyms;\n'
                      '3: You have hyperonyms and you want to classify your genitive groups;\n'
                      '4: Exit.\n'))
        if int(a) == 4:
            break
        if int(a) == 1:
            read_blank_file()
            print('Now you can find your corpus with Norm formes in file ./data/Data-set_normilized.csv\n'
                  'You can check for any errors occured while automatic parse\n'
                  'Print 2 to build corpus with hyperonyms.')
        if int(a) == 2:
            corpus = read_file_with_norm_forms()
            mark_corpus(corpus)
            print('Now you can find corpus with semantic tags in file ./result.csv\n'
                  'Print 3 to start classification.\n\n')
        if int(a) == 3:
            from set_labels import *
            data = read_file_with_sem_tags()
            try:
                set_rel(data[1:])
                print('Now you can find genitive groups with semantic relationship labels in ./feedback.txt\n')
            except:
                print('Error')
                pass
