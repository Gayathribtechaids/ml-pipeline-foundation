import logging


logger = logging.getLogger("ml_pipeline")

logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

file_handler = logging.FileHandler("pipeline.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)