import pandas as pd
import numpy as np

df_oem = pd.read_excel('C:/Users/isabe/Python/Excel/AlarmesOem.xlsx',engine='openpyxl')
dfapp_exa = pd.read_excel("C:/Users/isabe/Python/Excel/AppliExa.xlsx",engine='openpyxl')

df = df_oem[(df_oem['MetricGroup'] == 'ILOM SNMP Test Trap')]
for index,row in df.iterrows():
    host = df.at[index,'TargetName'].split('-',1)[0]
    code_app = (dfapp_exa.loc[(dfapp_exa['VM'].str.upper() == host.upper())]["CodeApplication"].head(1)).values
    if len(code_app) == 0 : 
        df.at[index,'CodeApplication'] = "XH_"
    else :
        df.at[index,'CodeApplication'] = code_app[0]
    df.at[index,'HOST'] = host
  
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.to_csv("./Sortie_CSV/Alarmes_OEM_2022_ILOMTest.csv")