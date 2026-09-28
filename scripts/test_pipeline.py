import sys
from ml_pipeline.exceptions import ProcessingError
from ml_pipeline.logger import logger
sys.path.append("src")

from ml_pipeline.pipeline import (
    Pipeline,
    LoadImageStep,
    ResizeImageStep
)


class ConvertToGrayscaleStep:
    def process(self, data):
        logger.info("Converting images to grayscale...")
        return data

pipeline = Pipeline([
    LoadImageStep(),
    ResizeImageStep(),
    ConvertToGrayscaleStep()
])

pipeline.run("image data")