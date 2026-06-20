import pandas as pd
from database.db_connect import engine
from typing import Dict
from logs.logger import ETLLogger

class SQLLoader :
    @staticmethod    
    def load_dfs(results : Dict[str,pd.DataFrame])->None:
        logger = ETLLogger.get_logger(__name__)
        for df_name ,  df in results.items():
            try:
                logger.info(f"injection dans la table SQL : {df_name}")
                df.to_sql(name=df_name , if_exists="append" , con=engine,index=False)
            except Exception as e :
                logger.error(f"erreur lors du loading dans : {df_name}")
                raise e