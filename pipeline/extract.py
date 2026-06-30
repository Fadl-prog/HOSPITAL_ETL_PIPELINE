import pandas as pd
import os
from typing import Dict
from logs.logger import ETLLogger

class CSVExtractor :
    
    @staticmethod

    def extract_multiple_csv(*paths : str) -> Dict[str , pd.DataFrame] :
    
        df_dict = {}
        logger = ETLLogger.get_logger(__name__)
        
        for path in paths :
            
            if not(os.path.exists(path)) :
                logger.error(f"the path does not exist : {FileNotFoundError}")
                raise FileNotFoundError("the file was not found")
            
            base_path,extension = os.path.splitext(path)
            
            if(extension.lower() != ".csv"):
                logger.error(f"the file is a {extension} file : {ValueError} ")
                raise ValueError("the file has to be a .csv")
             
            try:
                df_name = os.path.basename(base_path)
                df = pd.read_csv(path,encoding='utf-8')  
                df_dict[df_name] = df
                logger.info(f"the DataFrame named {df_name} of {df.shape[0]}")
            
            except Exception as e:
                logger.error(f"the following error occured while reading {path} : {e}")
                raise e
            
        return df_dict