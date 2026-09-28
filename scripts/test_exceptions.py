import sys

sys.path.append("src")

from ml_pipeline.exceptions import (
    DataError,
    ConfigurationError,
    ProcessingError
)


try:
    raise DataError("Invalid image data")
except DataError as error:
    print(f"Data error: {error}")


try:
    raise ConfigurationError("Invalid pipeline configuration")
except ConfigurationError as error:
    print(f"Configuration error: {error}")


try:
    raise ProcessingError("Image processing failed")
except ProcessingError as error:
    print(f"Processing error: {error}")