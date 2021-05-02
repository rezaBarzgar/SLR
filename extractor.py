from quickumls import QuickUMLS
import spacy
import subprocess


matcher = QuickUMLS('../SLR/QuickUMLS')
#text = "The ulna has dislocated posteriorly from the trochlea of the humerus."
text = "Plasma testosterone measurement humerus"
result = matcher.match(text, best_match=True, ignore_syntax=False)
cui = []
for item in result:
    cui.append(item[0]['cui'])
with open('../QueryExpantion/cuis.txt','w') as file:
    for item in cui:
        file.write(item+'\n')
    file.close()

