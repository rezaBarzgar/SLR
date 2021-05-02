import pymedtermino
from pymedtermino.umls import *
import time
import pandas


class UMLSGraph:
    def __init__(self):
        pymedtermino.LANGUAGE = "en"
        pymedtermino.REMOVE_SUPPRESSED_CONCEPTS = True
        connect_to_umls_db('localhost', 'root', 'sefteghoot', "umls", encoding="latin1")

    def create_graph(self, CUI):
        result = eval("UMLS_CUI[u\"{cui}\"].relations".format(cui=CUI))
        rel_list = []

        for item in result:
            try:
                temp = eval("UMLS_CUI[u\"{cui}\"].{item}".format(cui=CUI, item=item))
            except:
                pass
            for key in temp:
                print(key)
                rel_list.append(["UMLS_CUI[u\"{cui}\"]".format(cui=CUI), item, key])
        df = pandas.DataFrame(rel_list)
        print(df)
        df.to_csv('output.csv', index=False)

    def get_term(self, cui):
        return eval("UMLS_CUI[u\"{cui}\"].term".format(cui=cui))
