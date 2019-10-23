import spacy
import random
import plac
from spacy.lang.pt.examples import sentences
from spacy import displacy
nlp = spacy.load('pt_core_news_sm')
with open('../Docs/Corpus.txt', 'r', encoding='utf8') as sentencas:
    conteudo = sentencas.readlines()
annotation = []
for line in conteudo:
    sentenca = nlp(line.strip())
    sentence_annotation = []
    pos_annotation = []
    tag_annotation = []
    dep_annotation = []
    for token in sentenca:
        sentence_annotation.append('{}'.format(token.text))
        pos_annotation.append(token.pos_)
        tag_annotation.append(token.tag_)
        dep_annotation.append("{} = {}".format(token.dep_, token.head))
    annotation.append((sentence_annotation, pos_annotation,
                       tag_annotation, dep_annotation))
with open('Sentencas.csv', 'w', encoding="utf8") as output:
    for s, p, t, d in annotation:
        output.write("{}\n".format('***'.join(s)))
        output.write("{}\n".format('***'.join(p)))
        output.write("{}\n".format('***'.join(t)))
        output.write("{}\n".format('***'.join(d)))
