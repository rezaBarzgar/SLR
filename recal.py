import numpy as np

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
results = np.load('results.npy')
expandeds = np.load('pubmed_results.npy')
print(expandeds)
output = []
for i in range(len(expandeds)):
    title = expandeds[i,0]
    total = 0
    for res in results:
        if res[0] == title:
            total += 1
    print("total relevant for title "+title+" is : "+str(total))
    count = 0
    for item in expandeds[i,1]:
        for res in results:
            if res[0] == title:
                # print(res[0]+"----"+res[1])
                # print(title + "++++"+item[0])
                if res[1] == item[0]:
                    count += 1
    print("recall at 1000 for title "+title+" is : "+str(count/total))
    tempt = []
    tempt.append(title)
    tempt.append((count/total))
    output.append(tempt)
sum = 0
for item in output:
    sum += item[1]
print("avg recall is : "+str((sum/len(output))))
arr = np.array(output,dtype=object)
np.save('output_Recalls',arr)
