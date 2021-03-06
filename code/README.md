# Automatic Interpretation of Russian genitives

## Description

### Prerequisite

* Python3 installed
* Packages: pymorphy2, gensim
* Data-set in '.csv' format 

##### Expected data-set format:
* Columns:

```csv
| № | Пример | Вершина | Зависимое | Отношение | Грамм. признаки вершины | Грам. признаки зависимого | Производящее вершины | Производящее зависимого |
```
* Column 'Пример' should include    conext-sentence
* Column 'Вершина'                  - head-noun
* Column 'Зависимое'                - genitive-noun
* Column 'Грамм. признаки ...' should be formatted like this:
``` 
N(c|p)(m|f|n|c)(s|p)(n|g|d|a|i|l)(y|n)
    -   N = Noun
    -   c|p = {common|proper} name
    -   m|f|n|c = {masculin|feminine|neutrum|common} gender
    -   s|p = {singular|plural} number
    -   n|g|d|a|i|l = case
    -   y|n = {yes|no} animate
 ```
 * Column 'Производящее ...':
 
 ```
 A - derivated from Adjective ('красота' <- 'красивый')
 N - non-derivate Noun or derivated from Noun ('мама', 'кошка')
 Vt - derivated from transitive Verb ('обещать' <- 'обещание', 'открыть' <- 'открытие')
 Vn - derivated from non-transitive Verb ('беготня' <- 'бегать', 'дуновение' <- 'дуть')
 ```
 
 ## Program components
 
 ##### Python files
 ######  preprocess_corpus.py 
*   lemmatizing words with [pymorpy2](https://pymorphy2.readthedocs.io/en/latest/) 
*   creating set of hyperonyms based on [RuTez](http://www.labinform.ru/pub/ruthes/index.htm)
*   selecting the most relevant semantic category with [RusVectōrēs](https://rusvectores.org/ru/) *

\* From the selected list
###### set_sem_rel.py & set_labels.py
*   selecting semantic label for noun group

##### Other components
###### Folder [./data]:
* 'Data-set.csv' - initial data-set
* 'Data-set_normilized.csv' - lemmatized data-set

You are able to check for any mistakes occurred while automatic morph-parsing
######Folder [./sem_classes]
* Corpus based on linguistic ontology  [RuTez](http://www.labinform.ru/pub/ruthes/index.htm)

Also in folder [../data] you can find file 'rutez.py' which can help for updating corpus.
###### File result.csv 
* Here will be corpus with semantic tags set with classifier
Fileds are:

```
Гиперонимы вершины, Гиперонимы зависимого - based on RuTez 
Гиперонимы вершины WV, Гиперонимы зависимого WV - based on W2V
```
 
 ## Running program
 
 * Download folder
 * Run classificator.py with IDLE and follow the instruction
 


