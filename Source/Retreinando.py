from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
import csv
from spacy.symbols import ADJ, ADV, INTJ, NOUN, PROPN, VERB, ADP, AUX, CCONJ,DET, NUM, PRON, SCONJ, PUNCT, SYM, X 

TRAIN_DATA = []
nlp = spacy.load('pt_core_news_sm')

with open('../Docs/Sentencas.csv', 'r',encoding='utf8') as data_file:
    lines = data_file.readlines()
    i = 0
    while i < (len(lines)-1):
        tokens = lines[i].split("***")
        i += 1
        tags = lines[i].split("***")
        i += 1
        TRAIN_DATA.append(("{}".format(' '.join(tokens[:-1])), {"tags": tags[:-1]}))

TRAIN_DATA[:2]
random.shuffle(TRAIN_DATA)
print(len(TRAIN_DATA))
TEST_DATA = TRAIN_DATA[:43]
TRAIN_DATA = TRAIN_DATA[43:]

optimizer = nlp.begin_training()

test_text = "Apesar de estar doente, Maria foi para a escola hoje"
doc3 = nlp(test_text)
for token in doc3:
    print(token.text, token.pos_, token.dep_)  

for i in range(1):
    print("Epoch ", i)
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        try:
            nlp.update([text], [annotations], sgd=optimizer)
        except:
            print("Error on ", text, annotations)


nlp.to_disk('new_model')

tags_hits = 0
total_tags = 0


for text, reference in TEST_DATA:
    res = nlp(text)
    i = 0
    j=0
    for token in res:
        if token.pos_ == reference['tags'][i]:
            tags_hits += 1
        i += 1
        total_tags += 1
    j+=1

print("{} correct tags out of {}".format(tags_hits, total_tags))

doc3 = nlp(test_text)
for token in doc3:
    print(token.text, token.pos_, token.dep_)

