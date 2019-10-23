# Training: https://spacy.io/usage/training

from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from spacy.symbols import ADJ, ADV, INTJ, NOUN, PROPN, VERB, ADP, AUX, CCONJ,DET, NUM, PRON, SCONJ, PUNCT, SYM, X
# Criando mapa de tags
TAG_MAP = {"NOUN": {"pos": "NOUN"}, "VERB": {"pos": "VERB"}, "ADJ": {"pos": "ADJ"}, "PROPN": {"pos": "PROPN"},
          "ADV": {"pos": "ADV"}, "PUNCT": {"pos": "PUNCT"}, "INTJ":{"pos":"INTJ"},"DET":{"pos":"DET"},"X":{"pos":"X"}, "SYM":{"pos":"X"}, "ADP":{"pos":"ADP"},
          "SCONJ":{"pos":"SCONJ"},"CCONJ":{"pos":"CCONJ"}, "NUM":{"pos":"NUM"}, "AUX":{"pos":"AUX"},"PRON":{"pos":"PRON"}}

# Treinando dados
TRAIN_DATA = [
    ("Eu como ovos brancos", {"tags": ["NOUN", "VERB", "NOUN", "ADJ"]})
]

nlp = spacy.blank("pt")

# Adicionando as Tags
tagger = nlp.create_pipe("tagger")
for tag, values in TAG_MAP.items():
    tagger.add_label(tag, values)
nlp.add_pipe(tagger)

# Treinando
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
