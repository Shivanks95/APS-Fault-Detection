import pandas as pd
from sensor.config import mongo_client
from sensor.exception import SensorException
from sensor.logger import logging


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    try:
        logging.info(f"Reading Data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns: {df.columns}")
        if "_id" in df.columns:
            df = df.drop("_id", axis = 1)
    except Exception as e: 
        raise SensorException(e, sys)
