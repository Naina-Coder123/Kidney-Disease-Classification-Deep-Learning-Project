from src.cnnClassifier import logger

from src.cnnClassifier.pipeline.stage01_data_ingestion import DataingestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataingestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<< \n\nx=========x")
except Exception as e:
     logger.exception(e)
     raise e
