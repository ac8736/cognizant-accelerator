import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score, silhouette_score

# Load the Iris dataset from local txt file
df = pd.read_csv('iris.data.csv')

# Normalize the data
scaler = StandardScaler()
scaler.fit(df.drop('class', axis=1))
scaled_features = scaler.transform(df.drop('class', axis=1))
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df_feat)
    wcss.append(kmeans.inertia_)

optimal_clusters = 3
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(df_feat)

silhouette_avg = silhouette_score(df_feat, pred_y)
print("Silhouette Score:", silhouette_avg)

ari = adjusted_rand_score(df['class'], pred_y)
print("Adjusted Rand Index:", ari)

# plot 
plt.scatter(df_feat['sepal_length'], df_feat['sepal_width'], c=pred_y, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()
