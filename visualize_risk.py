import pandas as pd
import numpy as np
df = pd.DataFrame(columns= ['transaction_id', 'status', 'total_risk', 'customer_risk', 'country_risk', 'vessel_risk'])
for i in range(1,1000):
    status = np.random.choice(['Satisfactory', 'Unsatisfactory', 'Under Review'])
    if status=='Satisfactory':
        total_risk = np.random.randint(0, 100)
    elif status=='Unsatisfactory':
        total_risk = np.random.randint(100, 200)
    else:
        total_risk = 0
    values = np.random.rand(3)
    values = (values/np.sum(values))*total_risk
    customer_risk = values[0]
    country_risk = values[1]
    vessel_risk = values[2]
    df.loc[len(df)] = [i, status, total_risk, customer_risk, country_risk, vessel_risk]

df.to_csv('riskdata.csv')

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
colors = ['#DF2020', '#81DF20', '#2095DF']
kmeans = KMeans(n_clusters=3, random_state=1, n_init=10, max_iter=300)
df['cluster'] = kmeans.fit_predict(df[['country_risk', 'customer_risk', 'vessel_risk']])
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})
fig = plt.figure()
fig.tight_layout()
ax = plt.axes(projection='3d')
ax.scatter(df.customer_risk, df.country_risk, df.vessel_risk, c=df.c, s=15)
centers = kmeans.cluster_centers_
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2],  c='black',marker='*', s=100, alpha=0.5);
ax.set_xlabel('Country Risk')
ax.set_ylabel('Customer Risk')
ax.set_zlabel('Vessel Risk')
plt.title("K-Means clustering of Transaction Risk Data")
plt.savefig("kmeans.png")
plt.show()
    
# from autoviz.AutoViz_Class import AutoViz_Class
# AV=AutoViz_Class()
# viz = AV.AutoViz("riskdata.csv", sep=',', chart_format='html')