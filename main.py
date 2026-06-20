from pipeline.extract import CSVExtractor
from pipeline.load import SQLLoader
from pipeline.transform import MultipleDFTransformer
from logs.logger import ETLLogger
import os

def pipeline():
    logger = ETLLogger.get_logger(__name__)
    logger.info("debut de la pipeline")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    paths = [os.path.join(base_dir ,"data",filename) for filename in os.listdir("data")]
    df_dict = CSVExtractor.extract_multiple_csv(*paths)
    result = MultipleDFTransformer.transform_multiple_dfs(df_dict)
    SQLLoader.load_dfs(result)

if __name__ == "__main__":
    pipeline()