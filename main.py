
import nltk
nltk.download("wordnet")
nltk.download("names")

from nltk.corpus import wordnet
from nltk.corpus import names
import random

'''preparing variables'''
synonyms = []
antonyms = []
examples = []
tag = ''
word = "love"
syns = wordnet.synsets(word)


male_names = names.words('male.txt')
female_names = names.words('female.txt')

labeled_male_names = [(str(name), 'male') for name in male_names]
labeled_female_names = [(str(name), 'female') for name in female_names]

#labeled_all_names = labeled_male_names + labeled_female_names --> nicht gebraucht da je male und female names

random.shuffle(labeled_male_names)
random.shuffle(labeled_female_names)

#random names (from above), female + male(above), character char(in def)


def generate_names (char, num):
    labeled_male_names_char = []
    labeled_female_names_char = []
    num = int(input("How many names would you like to see?"))
    char = input("Which character should the names start with?")
    while i < num:
        if c >= len(labeled_female_names):
            break
        C = 0
        if labeled_female_names[c][0] == char:
            labeled_female_names_char.append(labeled_female_names[c])
            i = i+1
        C = c+1
        return labeled_female_names_char
    while i < num:
        if c >= len(labeled_male_names):
            break
        C = 0
        if labeled_male_names[c][0] == char:
            labeled_male_names_char.append(labeled_male_names[c])
            i = i + 1
        C = c + 1
        return labeled_male_names_char
    for i in labeled_female_names_char: #number2: add female and male names to txt files, only names tho
        with open("female_names.txt", "r") as reader:
            contents = reader.readlines()
        with open("female_names.txt", "w") as writer:
            for i in labeled_female_names_char:
                writer.write(name)
                writer.write('\n')
    for i in labeled_male_names_char:
        with open("male_names.txt", "r") as reader:
            contents = reader.readlines()
        with open("male_names.txt", "w") as writer:
            for i in labeled_male_names_char:
                writer.write(name)
                writer.write('\n')


#3

class SynAnt: # Implementing a class
    def __init__(self, names:lst):
        self.names = names

names = [love, friendship, sun, books]

    def find_synonyms(self): #printing out synonyms
        for i in names:
            for syn in syns:
                for l in syn.lemmas():
                    synonyms.append(l.name())
             if len(synonyms) == 0:
                synonyms.append("No synonyms found")
        print("Some synonyms of {} are: {}".format(word, set(synonyms)))


    def find_antonyms(self): #printing out antonyms
        for i in names:
            for syn in syns:
                for l in syn.lemmas():
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
                        if len(antonyms) == 0: #handling empty lists
                            antonyms.append("No antonyms found")
        print("Some antonyms of {} are: {}".format(word, set(antonyms)))






