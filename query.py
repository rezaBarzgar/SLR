import UMLSGraph
import recommender
from pubmed_query import pubmed_search
import pymed
from pymed import PubMed
import pandas as pd
from pandas import DataFrame as df
import numpy as np


def main():
    umls_graph = UMLSGraph.UMLSGraph()
    df = pd.read_csv('cui2vec_pretrained.csv')
    cui = []
    with open('cuis.txt','r') as file:
        Lines = file.readlines()
        for line in Lines:
            cui_list = recommender.recommender(line.rstrip("\n"), df)
            for item in cui_list:
                cui.append(item)
    terms = []
    for item in cui_list:
        term = umls_graph.get_term(item)
        terms.append(term)
    for term in terms:
        article_list = pubmed_search(term)
        for title in article_list:
            print(title)


if __name__ == '__main__':
    main()
