import sys

sys.path.append("src")

from ml_pipeline.pipeline import (
    Pipeline,
    LoadImageStep,
    ResizeImageStep
)


class ConvertToGrayscaleStep:

    def process(self, data):
        print("Converting images to grayscale...")
        return data


pipeline = Pipeline([
    LoadImageStep(),
    ResizeImageStep(),
    ConvertToGrayscaleStep()
])

pipeline.run("image data")