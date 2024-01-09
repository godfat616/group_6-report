#2005-2019期间各癌症在不同国家的患病率






from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


filepath4="04 share-of-population-with-cancer-types .csv"
df40=pd.read_csv(filepath4)
#print(df40)

#04表进行预处理
df41=df40[df40["Year"].isin([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])] #04表删去所有1990-2004年份的词条
df42=df41[df41["Entity"].isin(["China","United Kingdom","United States","Russia","Australia","Brazil","Ukraine","France","African Region (WHO)","Saudi Arabia"])] #04表留下待分析的十个国家
#print(df42)


df42.columns=["Entity","Code","Year","Liver cancer","Kidney cancer",
              "Larynx cancer","Breast cancer","Thyroid cancer","Bladder cancer",
              "Uterine cancer","Ovarian cancer","Stomach cancer","Prostate cancer",
              "Cervical cancer","Testicular cancer","Pancreatic cancer","Esophageal cancer",
              "Nasopharynx cancer","Colon and rectum cancer","Non-melanoma skin cancer",
              "Lip and oral cavity cancer","Brain and nervous system cancer",
              "Tracheal, bronchus, and lung cancer","Gallbladder and biliary tract cancer","Neoplasms"] #将列名换成简洁的癌症类型名，方便input
print(df42)



#可视化——图:2005-2019期间各癌症在不同国家地区的患病率
cancer_type=input("please input the cancer type:") #输入想要查询的癌症种类
plt.figure(dpi=80, figsize=(12, 8))
sns.lineplot(data=df42,x="Year",y=cancer_type,hue="Entity",style="Entity") #X轴是年份，y轴是输入的癌症的死亡率，以国家为分类呈现趋势
plt.title(f"Compare the rate of {cancer_type} prevalence every year between countries and areas")
plt.show()