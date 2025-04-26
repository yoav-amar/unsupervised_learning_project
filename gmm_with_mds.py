from ucimlrepo import fetch_ucirepo
import pandas as pd
import gower
from sklearn.metrics import silhouette_score
from sklearn.manifold import MDS
from sklearn.mixture import GaussianMixture


  
# fetch dataset 
adult = fetch_ucirepo(id=2) 
  
# data (as pandas dataframes) 
X = adult.data.features 
y = adult.data.targets 
  
new_df: pd.DataFrame = X

new_df = new_df[~new_df.eq("?").any(axis=1)]
new_df = new_df.dropna().reset_index(drop=True)
mini_df = new_df.sample(1000)

gower_dist = gower.gower_matrix(mini_df) 


mds = MDS(dissimilarity='precomputed')
X_embedded = mds.fit_transform(gower_dist)

scores = []
print("finish MDS")
# Fit GMM

for i in range(2, 20):
    gmm = GaussianMixture(n_components=i)
    labels = gmm.fit_predict(X_embedded)

    # Compute Silhouette Score
    score = silhouette_score(X_embedded, labels)
    print(f"Silhouette Score: {score:.3f}")
    scores.append(score)
    
import pickle


with open("gower_matrix_mds_gmm.pkl", "wb") as f:
    pickle.dump(scores, f)