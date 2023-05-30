import pandas as pd
import numpy as np

dfapp_exa = pd.read_excel("Excel/AppliExa.xlsx",engine='openpyxl')
df_oem = pd.read_excel('Excel/AlarmesOem.xlsx',engine='openpyxl')

df = df_oem[(df_oem ['MetricGroup'] == 'Resource State')] #Récupération du MetricGroup

for index, row in df.iterrows(): #Pour chaque index dans la colonne dans le dataframe
    df.at[index , 'Cluster'] = row['TargetName'] #On met les donnés de targeName à l'endroit spécifier
    cluster1 = row['TargetName']
    #On récupére le codeApplication ou le cluster est égale aux cluster de notre Alarmes et ensuite on récupére 
    #le CodeApplication . 
    code_app = (dfapp_exa.loc[(dfapp_exa['Cluster'].str.upper() == cluster1.upper()) ]["CodeApplication"]).head(1).values 

    if len(code_app) == 0 :
        code_app = (dfapp_exa.loc[(dfapp_exa['Cluster'].str.upper() == cluster1.upper()) ]["CodeApplication"]).head(1).values
        if len(code_app) == 0: #Donc si il y a plusieurs codeApplication on met XH_ 
            code_app = "XH_"   
        else : 
            code_app = str(code_app[0])
    else :
        code_app = code_app[0]
    df.at[index,'CodeApplication'] = code_app #On ecrit donc le code CodeApp à cet endroit

df.loc[df['TargetName'] == 'has_weya0333.net.intra.laposte.fr','CodeApplication'] = 'OM_'# Petite exeption dans lesquel j'attribue directement le codeApp
    
  
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # Ceci permet juste de ne récupérer que notre metricGroup dans le fichier que l'on modifie 
df.to_csv("./Sortie_CSV/Alarmes_OEM_2022_ResourceState.csv")#,sheet_name="Sheet1")#On transforme le DataFrame en CSV