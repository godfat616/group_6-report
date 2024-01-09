#图1：2005-2019期间全球癌症死亡占比
# Direction 1: 分析在2005-2019期间的世界人口，癌症在各个死亡原因中的占比
# • Aim:分析癌症对人口死亡率的影响程度
# • Data input:.csv文件：01 annual-number-of-deaths-by-cause & 02 total-cancer-deaths-by-type
# • Analysis:由折线图可知：2005至2019年期间，全球死亡人数中癌症的占比呈直线上升趋势。
#            分析可知：癌症对人类生命健康的影响越来越大，急需引起重视。
# • Visualization: "Global Cancer Mortality Rate in 2005-2019"



from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

filepath1="01 annual-number-of-deaths-by-cause.csv"
df10=pd.read_csv(filepath1)
#print(df10)

filepath2="02 total-cancer-deaths-by-type.csv"
df20=pd.read_csv(filepath2)
#print(df20)


#对01表进行预处理
df11=df10[df10["Year"].isin([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])] #01表删去所有1990-2004年份的词条
#print(df11)
df12=df11.groupby("Year").agg({"Deaths - Meningitis - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Alzheimer's disease and other dementias - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Parkinson's disease - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Nutritional deficiencies - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Malaria - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Drowning - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Maternal disorders - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Tuberculosis - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Lower respiratory infections - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Neonatal disorders - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Alcohol use disorders - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Self-harm - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Diarrheal diseases - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Environmental heat and cold exposure - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Neoplasms - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Conflict and terrorism - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Diabetes mellitus - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Chronic kidney disease - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Poisonings - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)":"sum","Terrorism (deaths)":"sum",
                         "Deaths - Road injuries - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Chronic respiratory diseases - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Cirrhosis and other chronic liver diseases - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Digestive diseases - Sex: Both - Age: All Ages (Number)":"sum",
                         "Deaths - Fire, heat, and hot substances - Sex: Both - Age: All Ages (Number)":"sum","Deaths - Acute hepatitis - Sex: Both - Age: All Ages (Number)":"sum"})
                         #01表以年份分组，将同年份的所有数据相加
df12["deaths_allcauses"]=(df12["Deaths - Meningitis - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Alzheimer's disease and other dementias - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Parkinson's disease - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Nutritional deficiencies - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Malaria - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Drowning - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Maternal disorders - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Tuberculosis - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Lower respiratory infections - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Neonatal disorders - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Alcohol use disorders - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Self-harm - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Diarrheal diseases - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Environmental heat and cold exposure - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Neoplasms - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Conflict and terrorism - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Diabetes mellitus - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Chronic kidney disease - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Poisonings - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)"]+df12["Terrorism (deaths)"]
                         +df12["Deaths - Road injuries - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Chronic respiratory diseases - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Cirrhosis and other chronic liver diseases - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Digestive diseases - Sex: Both - Age: All Ages (Number)"]
                         +df12["Deaths - Fire, heat, and hot substances - Sex: Both - Age: All Ages (Number)"]+df12["Deaths - Acute hepatitis - Sex: Both - Age: All Ages (Number)"])
                         #01表加一列所有原因的死亡数据总和

#print(df12)


#02表进行预处理
df21=df20[df20["Year"].isin([2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019])] #02表删去所有1990-2004年份的词条
df21["deaths_allcancers"]=(df21["Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Leukemia - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Pancreatic cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Esophageal cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Testicular cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Nasopharynx cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Other pharynx cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Colon and rectum cancer - Sex: Both - Age: All Ages (Number)"]
                        +df21["Deaths - Non-melanoma skin cancer - Sex: Both - Age: All Ages (Number)"]+df21["Deaths - Mesothelioma - Sex: Both - Age: All Ages (Number)"] )
                        #02表加一列所有癌症死亡人数的总和
#print(df21)
df22=df21.groupby("Year").agg({"deaths_allcancers":"sum"})  #02表以年份分组，将同年份的癌症死亡人数总和相加
#print(df22)

#将处理后的两个表合并
df30=pd.concat([df12,df22],axis=1)
df30["death_rate_cancers"]=df30["deaths_allcancers"]/df30["deaths_allcauses"] #03表加一列癌症死亡人数总和在总死亡人数中的占比
#print(df30)

#可视化——图1：2005-2019期间全球癌症死亡占比
sns.lineplot(data=df30,x="Year",y="death_rate_cancers")
plt.title("Global Cancer Mortality Rate in 2005-2019")
plt.show()




