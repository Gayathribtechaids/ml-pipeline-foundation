from abc import ABC, abstractmethod

from ml_pipeline.decorators import timeit, retry, ResourceManager
from ml_pipeline.logger import logger


class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass


class LoadImageStep(Step):

    def process(self, data):
        logger.info("Loading images...")
        return data


class ResizeImageStep(Step):

    def process(self, data):
        logger.info("Resizing images...")
        return data


class NormalizeImageStep(Step):

    def process(self, data):
        logger.info("Normalizing images...")
        return data


class Pipeline:

    def __init__(self, steps: list[Step]):
        self.steps = steps

    @timeit
    @retry(max_attempts=3)
    def run(self, data: object) -> object:
        with ResourceManager():
            for step in self.steps:
                data = step.process(data)

        return data