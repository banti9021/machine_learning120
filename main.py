'''from src.mlProject3 import logger
from src.mlProject3.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject3.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from src.mlProject3.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from src.mlProject3.pipeline.stage4_model_trainer import ModelTrainerTrainingPipeline
# from src.mlProject3.pipeline.model_evaluation import ModelEvaluationTrainingPipeline

def run_stage(stage_name, pipeline_class):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline_instance = pipeline_class()
        pipeline_instance.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    stages = [
        ("Data Ingestion stage", DataIngestionTrainingPipeline),
        ("Data Validation stage", DataValidationTrainingPipeline),
        ("Data Transformation stage", DataTransformationTrainingPipeline),
        ("Model Trainer stage", ModelTrainerTrainingPipeline),
        # ("Model Evaluation stage", ModelEvaluationTrainingPipeline),  # Uncomment if needed
    ]

    for stage_name, pipeline_class in stages:
        run_stage(stage_name, pipeline_class)'''
from src.mlProject3 import logger
from src.mlProject3.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject3.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from src.mlProject3.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from src.mlProject3.pipeline.stage4_model_trainer import ModelTrainerTrainingPipeline
from src.mlProject3.pipeline.stage5_model_evalution import ModelEvaluationTrainingPipeline

def run_stage(stage_name, pipeline_class):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline_instance = pipeline_class()
        pipeline_instance.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    stages = [
        ("Data Ingestion stage", DataIngestionTrainingPipeline),
        ("Data Validation stage", DataValidationTrainingPipeline),
        ("Data Transformation stage", DataTransformationTrainingPipeline),
        ("Model Trainer stage", ModelTrainerTrainingPipeline),
        ("Model Evaluation stage", ModelEvaluationTrainingPipeline),  # Uncomment if needed
    ]

    for stage_name, pipeline_class in stages:
        run_stage(stage_name, pipeline_class)
