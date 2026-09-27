# Day 4 — Type Hints & Pydantic for Configuration

## Objective

Create a validated configuration model for the image-processing pipeline using Python type hints and Pydantic.

## Implementation

Created `PipelineConfig` using Pydantic `BaseModel`.

Configuration fields:

- `data_path` — input image directory
- `batch_size` — number of images processed per batch
- `image_size` — target image size
- `mode` — pipeline execution mode
- `device` — processing device
- `confidence_threshold` — confidence threshold between 0 and 1

Created a `PipelineMode` Enum with:

- `train`
- `inference`

## Validation

Added validation for:

- Positive `batch_size`
- Positive `image_size`
- `confidence_threshold` between 0 and 1
- Valid pipeline mode using Enum
- Existing input directory
- Input path must be a directory

## Invalid Configuration Tests

### 1. Invalid Batch Size

```text
batch_size = -5

Result:

Input should be greater than 0
2. Invalid Pipeline Mode
mode = "testing"

Result:

Input should be 'train' or 'inference'
3. Nonexistent Data Path
data_path = "data/does_not_exist"

Result:

data_path does not exist


Key Concepts Learned
Python type hints
Pydantic BaseModel
Pydantic Field
Pydantic validators
Enum
Runtime validation
Configuration validation
Clear validation errors