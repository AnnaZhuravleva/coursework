import sys


import gensim
m = 'ruscorpora_mystem_cbow_300_2_2015.bin.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)
model.init_sims(replace=True)
words = ['президент_S', 'сын_S', 'рост_S', 'покупка_S', 'прыжок_S', 'толчок_S', 'дом_S']
cats = ['параметр_S', 'родственник_S', 'вещь_S', 'служащий_S', 'место_S', 'перемещать_S']

for word in words:
    for cat in cats:
        print(cat, word)
        print(model.similarity(cat, word))
