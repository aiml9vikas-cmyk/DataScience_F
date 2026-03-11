
from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.entity.config_entity import (DataIngestionConfig)

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info("welcome to data sciense first project")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logger.exception(e)
    raise e

