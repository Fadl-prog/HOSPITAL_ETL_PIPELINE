import pandas as pd
from database.db_connect import engine
from typing import Dict
from logs.logger import ETLLogger

class SQLLoader :
    @staticmethod    
    def load_dfs(results : Dict[str,pd.DataFrame])->None:
        order = ['dim_patient', 'dim_medecin', 'dim_departement', 'dim_date', 'fact_admission']
        logger = ETLLogger.get_logger(__name__)
        for df_name in order:
            if df_name in results.keys():
                try:
                    logger.info(f"injection dans la table SQL : {df_name}")
                    results[df_name].to_sql(name=df_name , if_exists="append" , con=engine,index=False)
                except Exception as e :
                    logger.error(f"erreur lors du loading dans : {df_name}")
                    raise e