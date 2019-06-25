# Training: https://spacy.io/usage/training

from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding

#Criando mapa de tags
TAG_MAP = {"N": {"pos": "NOUN"}, "V": {"pos": "VERB"}, "J": {"pos": "ADJ"}, "NNP":{"pos":"PROPN"},
"A":{"pos":"ADV"}, "P":{"pos":"PUNCT"}}

#Treinando dados
TRAIN_DATA = [
    ("Eu como ovos brancos", {"tags": ["N", "V", "N", "J"]}),
    ("Fala mano,blz ?",{"tags":["V", "J","P","A","P"]})
]

nlp = spacy.blank("pt")

#Adicionando as Tags
tagger = nlp.create_pipe("tagger")
for tag, values in TAG_MAP.items():
    tagger.add_label(tag, values)
nlp.add_pipe(tagger)

#Treinando
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], sgd=optimizer)

# testando o modelo treinado
test_text = "Eu como ovos brancos"
doc = nlp(test_text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

print("\n")

test_text2 = "Fala mano,blz ?"
doc2 = nlp(test_text2)
for token in doc2:
    print(token.text, token.pos_, token.dep_)

print("\n")

test_text3 = "Eae cara,blz ?"
doc3 = nlp(test_text3)
for token in doc3:
    print(token.text, token.pos_, token.dep_)
