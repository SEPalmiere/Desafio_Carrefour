import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import re

nlp = spacy.load('en_core_web_md')
doc = nlp("I sell apples to help me buy an Apple notebook")

print('___________________________________________________________________________________________________')
print('Text Tagging')
""" for token in doc:
    print(token.text, token.lemma_) """

for token in doc:
    print(f'{token.text:{15}} {token.lemma_:{15}} {token.pos_:{10}} {token.is_stop:}')

print('___________________________________________________________________________________________________')
print('Sintax Dependency')

for chunk in doc.noun_chunks:
    print(f'{chunk.text:{30}} {chunk.root.text:{15}} {chunk.root.dep_}')

print('___________________________________________________________________________________________________')
print('Name Entity Recognition')

for ent in doc.ents:
    print(ent.text, ent.label_)

print('___________________________________________________________________________________________________')
print('Sentence Segmentation')

doc1 = nlp("I am really loving to learn spacy. Spacy is a great python module. Next I will analyse the text emotion.")
for sent in doc1.sents:
    print(sent)

print('___________________________________________________________________________________________________')
print('Visualization Tool')

displacy.render(doc1, style = 'dep', options={'compact':True, 'distance': 100})
# Not showing in VScode, but its generate an image showing words relationships

print('___________________________________________________________________________________________________')
print('Text Interations')

text = "my phone number is 0116665896. Oh its too long, correct one is 055116665566."

print(re.search(r'\d{12}', text))
print(re.search(r'\d{10,12}', text))

print(re.findall(r'\w{10}',text))

print(re.findall(r'.h', text))

