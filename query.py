import UMLSGraph
import recommender
from pubmed_query import pubmed_search
import pymed
from pymed import PubMed
import pandas as pd
from pandas import DataFrame as df
import numpy as np


def expand_and_search(cui_list, df, graph):
    terms = []
    query = ''
    neighbours = []
    print(cui_list)
    for cui in cui_list:
        try:
            print('finding CUI nearest neighbours for {}'.format(cui))
            neigh = recommender.recommender(cui, df)
            for item in neigh:
                neighbours.append(item)
        except Exception as e:
            print('{} nabood'.format(cui))
    for item in neighbours:
        try:
            term = graph.get_term(item)
            print(term)
            terms.append(term)
        except Exception as e:
            print('terme {} nabood'.format(item))
    for term in terms:
        query = query + ' OR ' + term.replace(' ', ' OR ')
    print('THIS IS QUERY: {}'.format(query))
    print('---------------')
    results = pubmed_search(query)
    print('number of results: {}'.format(len(results)))
    print('---------------')
    return results


def main():
    umls_graph = UMLSGraph.UMLSGraph()
    df = pd.read_csv('E:\SLR\cui2vec_pretrained\cui2vec_pretrained.csv')
    np_load_old = np.load
    np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
    cuis = np.load('output_quickumls.npy')
    # print(cuis)
    results = []
    for i in range(len(cuis)):
        print('expanding {}'.format(cuis[i][0]))
        try:
            results.append([cuis[i][0], expand_and_search(list(cuis[i][1]), df, umls_graph)])
        except Exception as e:
            print('server connection broken')
    print(results)

    print('creating np array')
    pubmed_results = np.array(results, dtype=object)
    print('saving...')
    np.save('pubmed_results', pubmed_results)


if __name__ == '__main__':
    main()
