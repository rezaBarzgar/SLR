import pandas as pd
from sklearn.neighbors import NearestNeighbors


def recommender(cui1,df):
    cui = df.loc[df['Unnamed: 0'] == cui1]
    cui = cui.drop(['Unnamed: 0'], axis=1)
    df1 = df.drop(['Unnamed: 0'], axis=1)
    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(df1)
    distances, indices = nbrs.kneighbors(cui)
    indices = indices.tolist()
    cui_neigh = []

    for item in indices:
        cui_neigh.append(df.iloc[item]['Unnamed: 0'])

    cui_neigh = cui_neigh[0].tolist()
    return cui_neigh


if __name__ == '__main__':
    recommender('C0000163')

# [    1, 57478,     2, 58498,  6361, 42430, 57985, 23153, 10585, 26863]
