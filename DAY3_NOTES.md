# Day 3 — OOP for Pipelines: Composition Over Inheritance

## Objective

Build a modular image-processing pipeline using composition, where individual processing steps can be added or replaced without modifying the Pipeline class.

## Implementation

Created an abstract `Step` class using Python's `ABC` and `abstractmethod`.

Implemented concrete pipeline steps:

- `LoadImageStep`
- `ResizeImageStep`
- `NormalizeImageStep`

Created a `Pipeline` class that accepts a list of Step objects and executes them sequentially.

## Composition Over Inheritance

The `Pipeline` class does not inherit from individual processing steps.

Instead, it receives Step objects through composition.

This allows processing steps to be changed or replaced without modifying the Pipeline implementation.

## Runtime Step Swapping

Tested replacing `NormalizeImageStep` with a new `ConvertToGrayscaleStep`.

The Pipeline class did not require any changes.

Output:

```text
Loading images...
Resizing images...
Converting images to grayscale...