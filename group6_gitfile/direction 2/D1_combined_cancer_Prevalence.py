import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('07 share-of-population-with-cancer-by-age.csv')

# 国家列表
countries = ["Kuwait", "South Korea", "Ukraine", "Poland", "Greenland", "Egypt", "Turkey", "France", "Andorra", "Mongolia"]
# 创建一个大图，分为2行5列
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(20, 10))
fig.tight_layout(pad=4.0)

# 遍历国家列表
for i, country in enumerate(countries):
    # 计算当前国家在大图中的位置
    row, col = divmod(i, 5)

    # 在对应的子图中绘制数据
    ax = axes[row, col]
    country_data = df[df['Entity'] == country]
    columns_of_interest = ['Year',
                            'Prevalence - Neoplasms - Sex: Both - Age: Under 5 (Percent)',
                           'Prevalence - Neoplasms - Sex: Both - Age: 5-14 years (Percent)',
                            'Prevalence - Neoplasms - Sex: Both - Age: 15-49 years (Percent)',
                            'Prevalence - Neoplasms - Sex: Both - Age: 50-69 years (Percent)',
                            'Prevalence - Neoplasms - Sex: Both - Age: 70+ years (Percent)',
                            'Prevalence - Neoplasms - Sex: Both - Age: All Ages (Percent)']
    selected_data = country_data[columns_of_interest]
    selected_data.set_index('Year', inplace=True)

    for column in selected_data.columns:
        ax.plot(selected_data.index, selected_data[column], label=column)

    ax.set_title(f'{country}')
    ax.set_xlabel('Year')
    ax.set_ylabel('prevalence (Percent)')
    # 设置纵轴范围
    ax.set_ylim(0, 14)

    # 在整个图的右边添加 legend
    if i == 4:
        ax.legend(title='Age Group', bbox_to_anchor=(1.05, 0.5), loc='center left')

# 保存大图
plt.savefig('combined_cancer_Prevalence.png')

# 显示大图
plt.show()
