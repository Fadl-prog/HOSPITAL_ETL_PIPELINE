import logging
import os

class ETLLogger :
    @staticmethod
    def get_logger(name : str) -> logging.Logger:
        logger = logging.getLogger(name)
  
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            log_path = os.path.join(base_dir,"logs","etl_pipeline.log")
            file_handler = logging.FileHandler(log_path, encoding = 'utf-8')
            file_handler.setLevel(logging.INFO)

            formatter = logging.Formatter("%(asctime)s - %(name)s - %(filename)s - %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

