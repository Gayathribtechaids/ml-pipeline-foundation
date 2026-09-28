import sys

sys.path.append("src")

from ml_pipeline.pipeline import (
    Pipeline,
    LoadImageStep,
    ResizeImageStep
)
from ml_pipeline.logger import logger


class ConvertToGrayscaleStep:

    def process(self, data):
        logger.info("Converting images to grayscale...")
        return data


class NormalizeCustomStep:

    def process(self, data):
        logger.info("Applying custom normalization...")
        return data


pipeline = Pipeline([
    LoadImageStep(),
    ResizeImageStep(),
    ConvertToGrayscaleStep(),
    NormalizeCustomStep()
])

pipeline.run("image data")