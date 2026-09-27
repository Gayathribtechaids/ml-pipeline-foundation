from pathlib import Path
from PIL import Image


class BatchIterator:

    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        batch = self.data[self.index:self.index + self.batch_size]

        self.index += self.batch_size

        return batch


class ImageBatchIterator:

    def __init__(self, folder_path, batch_size):
        if batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")

        self.folder_path = Path(folder_path)
        self.batch_size = batch_size
        self.image_paths = self.folder_path.glob("*.jpg")

    def __iter__(self):
        return self

    def __next__(self):
        batch = []

        for _ in range(self.batch_size):
            try:
                image_path = next(self.image_paths)
            except StopIteration:
                break

            with Image.open(image_path) as image:
                batch.append(image.copy())

        if not batch:
            raise StopIteration

        return batch