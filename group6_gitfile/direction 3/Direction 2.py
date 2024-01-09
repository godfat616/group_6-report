# 2005-2019期间各癌症在不同国家地区的死亡率
# Direction 2: 分析在2005-2019期间的中国，英国，美国，俄罗斯，法国，澳大利亚，非洲地区，巴西，乌克兰，沙特这几个国家中，各个癌症的死亡率
# • Aim:分析不同类型的癌症在不同地区的致死率对比
# • Data input:癌症类型      .csv文件： 02 total-cancer-deaths-by-type
# • Analysis:分析可知，在2005-2019期间，一些癌症的致死率在所有国家地区中整体都呈下降趋势，如胃癌；一些癌症的致死率呈上升趋势，如肾癌；
#            一些癌症的死亡率呈波动趋势，如肝癌；一些癌症的死亡率在不同国家地区的趋势不同，如乳腺癌。
#            也可以根据国家纵向分析，如对于中国来说，乳腺癌与肾癌的死亡率较低，而胃癌与肝癌的死亡率较高，这或许与我国的生活饮食习惯有关。
# • Visualization:"Compare the death rate of {cancer_type} every year between countries and areas"


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

filepath3="02 total-cancer-deaths-by-type.csv"
df30=pd.read_csv(filepath3)
#print(df30)

#02表进行预处理
df31=df30[df30["Year"].isin([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])] #02表删去所有1990-2004年份的词条
df31["deaths_allcancers"]=(df31["Deaths - Liver cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Leukemia - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Pancreatic cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Esophageal cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Testicular cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Nasopharynx cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Other pharynx cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Colon and rectum cancer - Sex: Both - Age: All Ages (Number)"]
                        +df31["Deaths - Non-melanoma skin cancer - Sex: Both - Age: All Ages (Number)"]+df31["Deaths - Mesothelioma - Sex: Both - Age: All Ages (Number)"] )
                        #02表加一列所有癌症死亡人数的总和
df32=df31[df31["Entity"].isin(["China","United Kingdom","United States","Russia","Australia","Brazil","Ukraine","France","African Region (WHO)","Saudi Arabia"])] #02表留下待分析的十个国家
#print(df32)

df33=df32.groupby(["Year","Entity"]).agg({"Deaths - Liver cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Leukemia - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Pancreatic cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Esophageal cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Testicular cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Nasopharynx cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Other pharynx cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Colon and rectum cancer - Sex: Both - Age: All Ages (Number)":"sum",
                        "Deaths - Non-melanoma skin cancer - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Mesothelioma - Sex: Both - Age: All Ages (Number)":"sum","deaths_allcancers":"sum"})
                         #02表以年份与国家分组，将同年份中相同的国家的所有数据相加
#print(df33)

df33["Kidney cancer"]=df33["Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Lip and oral cavity cancer"]=df33["Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Tracheal, bronchus, and lung cancer"]=df33["Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Larynx cancer"]=df33["Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Gallbladder and biliary tract cancer"]=df33["Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Malignant skin melanoma"]=df33["Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Liver cancer"]=df33["Deaths - Liver cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Leukemia"]=df33["Deaths - Leukemia - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Hodgkin lymphoma"]=df33["Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Multiple myeloma"]=df33["Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Other neoplasms"]=df33["Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Breast cancer"]=df33["Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Prostate cancer"]=df33["Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Thyroid cancer"]=df33["Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Stomach cancer"]=df33["Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Bladder cancer"]=df33["Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Uterine cancer"]=df33["Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Ovarian cancer"]=df33["Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Cervical cancer"]=df33["Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Brain and central nervous system cancer"]=df33["Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Non-Hodgkin lymphoma"]=df33["Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Pancreatic cancer"]=df33["Deaths - Pancreatic cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Esophageal cancer"]=df33["Deaths - Esophageal cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Testicular cancer"]=df33["Deaths - Testicular cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Nasopharynx cancer"]=df33["Deaths - Nasopharynx cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Other pharynx cancer"]=df33["Deaths - Other pharynx cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Colon and rectum cancer"]=df33["Deaths - Colon and rectum cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Non-melanoma skin cancer"]=df33["Deaths - Non-melanoma skin cancer - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
df33["Mesothelioma"]=df33["Deaths - Mesothelioma - Sex: Both - Age: All Ages (Number)"]/df33["deaths_allcancers"]
#计算每个癌症类型的死亡率，并添加至列

#print(df33)
df34=df33.reset_index()
#print(df34)

#可视化——图:2005-2019期间各癌症在不同国家地区的死亡率
cancer_type=input("please input the cancer type:") #输入想要查询的癌症种类
plt.figure(dpi=80, figsize=(8, 8))
sns.scatterplot(data=df34,x="Year",y=cancer_type,hue="Entity",style="Entity",size=cancer_type) #X轴是年份，y轴是输入的癌症的死亡率，以国家为分类呈现趋势
plt.title(f"Compare the death rate of {cancer_type} every year between countries and areas")
plt.show()

