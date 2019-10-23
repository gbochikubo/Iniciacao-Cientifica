from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
import csv
from spacy.symbols import ADJ, ADV, INTJ, NOUN, PROPN, VERB, ADP, AUX, CCONJ,DET, NUM, PRON, SCONJ, PUNCT, SYM, X

#Função responsável por formatar as frases retiradas do arquivo csv
def formataFrase(lista):
    simbolos_especiais = ['.', ',', ':', ';', '?', '!', '...']
    frase = ""  
    tamanho = len(lista)

    atual = 0

    while atual < tamanho:
        elemento = lista[atual]
        if elemento in simbolos_especiais or atual == 0:
            frase += elemento
        else:
            frase += " " + elemento

        atual = atual + 1
    
    return frase

#arquivo Sentancas
annotationSentencas = []
#arquivo teste
annotationTeste =[]
#sentencas
sentence_annotation = []
#pos 
pos_annotation = []
nlp = spacy.load('pt_core_news_sm')

#Lendo as sentencas do arquivo Sentencas.csv
with open('../Docs/Sentencas.csv','r', encoding='utf8') as sentencas:
    reader = sentencas.readlines()
    for line in reader:
        annotationSentencas.append(line.split('***'))

sentencas.close()

#Lendo a pos corrigida das sentencas do arquivo posAnnotations.csv
with open('../Docs/posAnnotations.csv','r',encoding='utf8') as pos:
    reader = pos.readlines()
    for line in reader:
        annotationTeste.append(line.split(','))


#Adicionando somente as sentencas a lista annotationSentencas
contador = 0
while(contador<837):
    sentence_annotation.append(annotationSentencas[contador])
    contador = contador+4

#Adicionando somente a pos na lista pos_annotation
contador = 0
while(contador<=419):
    if(contador%2 == 1):
        pos_annotation.append(annotationTeste[contador])
    contador = contador+1

#Removendo os espaços em branco do final de cada pos annotation
i = 0
j = 0
while(i<210):
    while(j<28):
        if(pos_annotation[i][j]==''):
            del pos_annotation[i][j-1:28]
            j=28
        j = j + 1   
    j=0
    i = i +1


print(formataFrase(sentence_annotation[0]))

TRAIN_DATA = []

atual = 0
while atual < len(sentence_annotation):
    elemento = (formataFrase(sentence_annotation[atual]), {"tags": pos_annotation[atual]})
    TRAIN_DATA.append(elemento)

    atual = atual + 1

#print(TRAIN_DATA)

# Treinando
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        #print("TEXT : ", len(text))
        #print("ANNOTATIONS : ", len(annotations))
        #print(annotations)
        nlp.update([text], [annotations], sgd=optimizer)
