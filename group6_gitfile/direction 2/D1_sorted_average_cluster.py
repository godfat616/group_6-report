import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 读取数据
df = pd.read_csv('03 cancer-death-rates-by-age.csv')

# 选择需要的列
columns_of_interest = ['Entity', 'Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)']
selected_data = df[columns_of_interest]

# 按国家分组，并计算每个国家的平均值
average_rates = selected_data.groupby('Entity')['Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)'].mean().reset_index()

# 排序平均值
sorted_average_rates = average_rates.sort_values(by='Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)', ascending=True)

# 可视化显示
plt.figure(figsize=(12, 6))
plt.scatter(sorted_average_rates['Entity'], sorted_average_rates['Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)'], color='skyblue', s=10)
plt.xticks([])  # 隐藏横坐标标签
plt.title('Average Cancer Death Rates (Age-standardized) by Country')
plt.xlabel('Country')
plt.ylabel('Average Death Rate')
plt.savefig('Age_standardized_death_rates.png')
plt.show()
#############################################
#
########### 聚类，不同国家分为五类 ##############
#
#############################################

# 选择列
selected_data = sorted_average_rates[['Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)']]

# 标准化数据
scaler = StandardScaler()
scaled_data = scaler.fit_transform(selected_data)

# 使用 K-Means 聚类
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
sorted_average_rates['Cluster'] = kmeans.fit_predict(scaled_data)

# 可视化显示
plt.figure(figsize=(12, 6))

# 绘制每个国家的平均死亡率
scatter=plt.scatter(sorted_average_rates['Entity'], sorted_average_rates['Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)'],
            c=sorted_average_rates['Cluster'], cmap='viridis', s=10)

plt.xticks([])  # 隐藏横坐标标签
plt.title('Average Cancer Death Rates (Age-standardized) by Country')
plt.xlabel('Country')
plt.ylabel('Average Death Rate')

# 添加颜色图例
legend_labels = [f'Cluster {i+1}' for i in range(5)]
plt.legend(handles=scatter.legend_elements()[0], labels=legend_labels, title='Cluster')
plt.savefig('Age_standardized_death_rates_cluster.png')
plt.show()
# 打开一个文件，如果不存在则创建
with open('cluster_info.txt', 'w') as file:
    # 显示每个簇中的国家及其平均值
    for cluster in sorted_average_rates['Cluster'].unique():
        cluster_data = sorted_average_rates[sorted_average_rates['Cluster'] == cluster]
        for index, row in cluster_data.iterrows():
            line = f'Cluster {cluster + 1}: Country: {row["Entity"]}, Average Rate: {row["Deaths - Neoplasms - Sex: Both - Age: Age-standardized (Rate)"]}\n'
            # 将信息写入文件
            file.write(line)

print("Cluster information has been written to 'cluster_info.txt'")