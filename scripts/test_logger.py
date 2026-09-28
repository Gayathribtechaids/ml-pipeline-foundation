import sys

sys.path.append("src")

from ml_pipeline.logger import logger


logger.info("Pipeline started")
logger.warning("Test warning message")
logger.error("Test error message")