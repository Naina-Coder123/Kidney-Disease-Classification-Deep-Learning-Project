from src.cnnClassifier import logger

from src.cnnClassifier.pipeline.stage01_data_ingestion import DataingestionTrainingPipeline
from src.cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage03_model_training import ModelTraningPipeline
from src.cnnClassifier.pipeline.stage04_model_evaluation_mlflow import EvaluationPipeline

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
    

STAGE_NAME= "TRAINING"
if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=ModelTraningPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME= "Evaluation stage"
if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<< \n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e