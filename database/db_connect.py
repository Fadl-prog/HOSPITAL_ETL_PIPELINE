from sqlalchemy import create_engine
from dotenv import load_dotenv
from logs.logger import ETLLogger
import os

logger = ETLLogger.get_logger(__name__)
try:

    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")
    db_url = f"mysql+pymysql://{user}:{password}@{host}/{name}"
    engine = create_engine(url=db_url)
    logger.info(f"succesfully connected to the database : {name}")

except Exception as e:
    logger.exception(e)
    raise Exception(f"there was an error during the connection to the database : {e}")
