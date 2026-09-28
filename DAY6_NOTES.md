# Day 6 — Custom Exceptions

## Objective

Create project-specific exceptions and use them in the ML pipeline.

## Custom Exception Hierarchy

PipelineError
├── DataError
├── ConfigurationError
└── ProcessingError

## Why Custom Exceptions?

Custom exceptions make pipeline errors easier to understand and handle.

Instead of using only generic exceptions, different failures can be identified based on their purpose.

## Exception Handling

`ProcessingError` is used for errors that occur during pipeline processing.

The retry decorator was updated to catch only `ProcessingError` instead of catching every `Exception`.

This prevents unrelated errors from being retried unnecessarily.

## Testing

The custom exceptions were tested independently.

A temporary `ProcessingError` was also raised inside the pipeline to verify that:

- The custom exception was correctly raised.
- The retry mechanism handled `ProcessingError`.
- The resource manager released the resource after each failed attempt.
- The final exception was propagated.

## Result

Day 6 successfully implemented custom exception classes and integrated `ProcessingError` with the pipeline retry mechanism.