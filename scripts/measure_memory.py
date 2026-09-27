import sys
import tracemalloc

sys.path.append("src")

from ml_pipeline.data_iterator import ImageBatchIterator
tracemalloc.start()

iterator = ImageBatchIterator("data/raw", batch_size=10)

for batch in iterator:
    pass

current, peak = tracemalloc.get_traced_memory()

print(f"Current memory: {current / 1024:.2f} KB")
print(f"Peak memory: {peak / 1024:.2f} KB")

tracemalloc.stop() 