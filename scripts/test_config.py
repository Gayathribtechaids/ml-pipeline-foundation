import sys

sys.path.append("src")

from ml_pipeline.config import PipelineConfig


config = PipelineConfig(
    data_path="data/raw",
    batch_size=10,
    image_size=224,
    mode="inference",
    device="cpu",
    confidence_threshold=0.8
)

print(config)