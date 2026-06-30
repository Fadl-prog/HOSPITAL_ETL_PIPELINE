
import time
from sqlalchemy import create_engine
from dotenv import load_dotenv
from logs.logger import ETLLogger
import os

logger = ETLLogger.get_logger(__name__)

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
name = os.getenv("DB_NAME")
db_url = f"mysql+pymysql://{user}:{password}@{host}/{name}"


engine = None
max_retries = 10
for i in range(max_retries):
    try:
        logger.info(f"Tentative de connexion à la base {name} (essai {i+1}/{max_retries})...")
        engine = create_engine(url=db_url)
        # Test réel de la connexion
        with engine.connect() as connection:
            logger.info(f"Connexion à la base de données '{name}' réussie !")
            break # On sort de la boucle si ça marche
    except Exception as e:
        logger.warning(f" MySQL n'est pas encore prêt. Attente de 5s...")
        time.sleep(5)
else:
    logger.error("Impossible de se connecter à la base de données après plusieurs tentatives.")
    raise Exception("Database connection failed after retries.")
