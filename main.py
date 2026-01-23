from src.cnnClassifier import logger

from src.cnnClassifier.pipeline.stage01_data_ingestion import DataingestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataingestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<< \n\nx=========x")
except Exception as e:
     logger.exception(e)
     raise e
 
 
 

 
STAGE_NAME="Prepare base model"
if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
