# SLR
This repository contains files to increase recall for expert user's query using PubMed.
The methods which used in this repository for increasing recall is query expansion.
Two kind of embedding is used for query expansion:
  •	CUI2VEC
    o	You can find more information from this link:  http://cui2vec.dbmi.hms.harvard.edu/
  •	BIOWORD2VEC
    o	You can find more information from this link:  https://github.com/ncbi-nlp/BioWordVec
It is necessary to load UMLS database on your local database. You can download the UMLS from link below:
https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html

Libraries which used in this project:
  •	QuickUMLS
  •	Pymedtermino
  •	Pymed

Step one:
  By using QuickUMLS we extract relevant concepts for each query string. In UMLS each concept is stored as a CUI in UMLS database. Relevant codes are represented in ----------
Step two:
  After extracting CUIs from each query we used Pymedtermino for finding which terms are mapped to each CUI. For each CUI there is a main term and several other alternative terms.
Step three:
	CUI2VEC:
    In this embedding each term represented by a vector. After loading CUI2VEC dataset, for previous step terms we find nearest vectors by using Sklearn Nearest Neighbors library. 
	BIOWORD2VEC:
    This embedding is more comprehensive than CUI2VEC. Is contains 2M words that presented by vectors. BIOWORD2VEC can be loaded by genism KeyedVectors. This library provides some     useful functions for finding most similar words .In this step we create a string for each CUI by utilizing prior step terms in this pattern: [MAIN TERM + ‘means’ + ALTERNATIVE     TERMS]. In this embedding all of the words are in lowercase and there is no stop words. So we need to remove stop words and change whole query to lowercase. Now we find most       similar words and adding them to initial query.
Last Step:
  Pymed library is used to search expanded query. This API returns various information about each article but we just print out article’s title and article’s summery.
	
