from enum import Enum
from pydantic import BaseModel, Field, field_validator
from pydantic import BaseModel
from pathlib import Path
from pydantic import BaseModel, Field

class PipelineMode(str, Enum):
    TRAIN = "train"
    INFERENCE = "inference"

class PipelineConfig(BaseModel):
    data_path: Path
    batch_size: int = Field(gt=0)
    image_size: int = Field(gt=0)
    mode: PipelineMode
    device: str = "cpu"
    confidence_threshold: float = Field(ge=0.0, le=1.0)
    
    @field_validator("data_path")
    @classmethod
    def validate_data_path(cls, value):
        if not value.exists():
            raise ValueError("data_path does not exist")

        if not value.is_dir():
            raise ValueError("data_path must be a directory")

        return value