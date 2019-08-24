import spacy
import random
import plac
from spacy.lang.pt.examples import sentences
from spacy import displacy
nlp = spacy.load('pt_core_news_sm')
arquivo = open('Corpus.txt','r')
sentencas = open('Sentencas.txt','r')
conteudo = sentencas.readlines()
for line in arquivo:
    sentenca = nlp(line)
    for token in sentenca:
        conteudo.append(token.text)
        conteudo.append("\n")
        conteudo.append(token.pos_)
        conteudo.append("\n")
        conteudo.append(token.dep_)
        conteudo.append("\n")
        conteudo.append("\n")
    conteudo.append("-------------------------------------------------------------------------------------------------------------------------")
    conteudo.append("\n")
sentencas = open('Sentencas.txt','w')
sentencas.writelines(conteudo)
arquivo.close()
sentencas.close()
