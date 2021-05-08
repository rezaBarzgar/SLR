from quickumls import QuickUMLS
import spacy
import subprocess
import glob
import numpy as np

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
topics = np.load('topics.npy')
# output = np.load('output_quickumls.npy')
# print(output)
matcher = QuickUMLS('../SLR/QuickUMLS')
output = []
for i in range(len(topics)):
    res = []
    print(topics[i,1])
    result = matcher.match(topics[i,1], best_match=True, ignore_syntax=False)
    cui = []
    for item in result:
        cui.append(item[0]['cui'])
    res.append(topics[i,0])
    res.append(cui)
    output.append(res)
arr = np.array(output,dtype=object)
np.save('output_quickumls',arr)

