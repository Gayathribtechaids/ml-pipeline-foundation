from abc import ABC, abstractmethod
class Step(ABC):

    @abstractmethod
    def process(self, data):
        pass
class LoadImageStep(Step):

    def process(self, data):
        print("Loading images...")
        return data
    
class ResizeImageStep(Step):

    def process(self, data):
        print("Resizing images...")
        return data
    
class NormalizeImageStep(Step):

    def process(self, data):
        print("Normalizing images...")
        return data
    
class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step.process(data)
        return data
    