import pandas as pd
from typing import Dict
from logs.logger import ETLLogger
import numpy as np

class MultipleDFTransformer : 
    @staticmethod
    def transform_multiple_dfs(df_dict : Dict[str , pd.DataFrame])->Dict[str,pd.DataFrame]:
        result : Dict[str , pd.DataFrame] = dict()
        logger = ETLLogger.get_logger(__name__)

        for df_name , df in df_dict.items():
            
            try:
                df = df.copy()

                logger.info(f"transformation of the dataframe named : {df_name} , initial size : {df.shape[0]}")
                #transformations applied on all the dataframes : 

                df.drop_duplicates(inplace=True)
                df.dropna(subset=[df.columns[0]],inplace=True)

                #specific transformations per each csv 

                #dim_patient transformations
                if df_name == "dim_patient" :

                    #Formater les strings pour faire en sorte que toutes les colonnes strings soient stripper

                    df[['prenom_patient','nom_patient','sexe_patient','num_dossier_patient','ville_patient']] =  df[['prenom_patient','nom_patient','sexe_patient','num_dossier_patient','ville_patient']].apply(lambda col : col.fillna('unknown').str.strip())
                    #capitaliser les colonnes nom , prenom , ville
                    df[['prenom_patient','nom_patient','ville_patient']] = df[['prenom_patient','nom_patient','ville_patient']].apply(lambda col : col.str.lower().str.capitalize())
                    #upper la colonne dossier
                    df['num_dossier_patient'] = df['num_dossier_patient'].str.upper()
                    
                    #nettoyer les colonnes age , sexe et dossier pour faire en sorte d'enlever les valeurs aberrantes
                    df = df[df['age_patient'].fillna(0).astype(int).between(0,120)]
                    df = df[df['sexe_patient'].str.upper().isin(['M','F','UNKNOWN'])]
                    df = df[df['num_dossier_patient'].str.match(r"^DOS.*")]
                
                #dim_medecin transformations
                elif df_name == "dim_medecin":
                    #ici , il n'y'a que le formattage des strings qui soit vraiment utile
                    df[df.columns[1:]] = df[df.columns[1:]].apply(lambda col : col.str.strip().str.lower().str.capitalize())

                #dim_departement transformations
                elif df_name == "dim_departement" :
                    df[df.columns[1:]] = df[df.columns[1:]].apply(lambda col : col.str.strip())

                #dim_date transformations
                elif df_name == "dim_date" :
                    df = df.fillna(-1)
                    df['date_complete'] = pd.to_datetime(df['date_complete'],errors = 'coerce')
                    df[['mois_date','jour_sem_date','annee_date']] = df[['mois_date','jour_sem_date','annee_date']].astype(int)
                
                #dim_medicament transformations
                elif df_name == "dim_medicament":
                    df[['nom_medicament','description_medicament']] = df[['nom_medicament','description_medicament']].apply(lambda col:col.str.strip().str.lower().str.capitalize())
                
                #fact_admission transformations
                elif df_name == "fact_admission":
                    df.dropna(subset=['id_patient','id_medecin','id_departement','id_date'],inplace=True)
                    df['cout_hebergement'] = df['cout_hebergement'].fillna(value='0')
                    df['cout_hebergement'] = df['cout_hebergement'].astype(float)
                    df['cout_soins_infirmiers'] = df['cout_soins_infirmiers'].fillna(value='0')
                    df['cout_soins_infirmiers'] = df['cout_soins_infirmiers'].astype(float)
                    df['duree_sejour'] = df['duree_sejour'].astype(int)
                    df['cout_total'] = df['cout_hebergement']+df['cout_soins_infirmiers']
                    df['cout_par_jour'] = np.where(df['duree_sejour'] > 0,df['cout_total']/df['duree_sejour'],df['duree_sejour'])
                
                #fact_ordonnace transformations
                elif df_name == "fact_ordonnance":
                    df.dropna(subset=['id_patient','id_medecin','id_date','id_medicament'],inplace=True)
                
                logger.info(f"the df : {df_name} was transformed and ended up with {df.shape[0]} rows")

                result[df_name] = df
            except Exception as e:

                logger.error(f"the following error {e} occured during the transformation of {df_name}")
                raise e
        return result