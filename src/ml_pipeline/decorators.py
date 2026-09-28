import time
from functools import wraps
from ml_pipeline.exceptions import ProcessingError

def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")

        return result

    return wrapper
def retry(max_attempts):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except ProcessingError:
                    attempts += 1

                    if attempts == max_attempts:
                        raise

                    print(f"Retrying {func.__name__}...")

        return wrapper

    return decorator
class ResourceManager:

    def __enter__(self):
        print("Resource acquired")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")
        return False