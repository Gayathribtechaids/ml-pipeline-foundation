import sys

sys.path.append("src")

from ml_pipeline.data_iterator import ImageBatchIterator


iterator = ImageBatchIterator("data/raw", batch_size=10)

batch_count = 0

for batch in iterator:
    batch_count += 1

print(f"Total batches processed: {batch_count}")