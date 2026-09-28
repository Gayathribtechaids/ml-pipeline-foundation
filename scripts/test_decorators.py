import sys
import time

sys.path.append("src")

from ml_pipeline.decorators import timeit, retry, ResourceManager


@timeit
def process_data():
    time.sleep(1)
    print("Data processed")


attempt_count = 0


@retry(max_attempts=3)
def unreliable_process():
    global attempt_count

    attempt_count += 1

    if attempt_count < 3:
        raise ValueError("Temporary processing failure")

    print("Processing successful")


print("Testing @timeit:")
process_data()

print("\nTesting @retry:")
unreliable_process()

print("\nTesting context manager:")
with ResourceManager():
    print("Using resource")