# Day 5 — Decorators, Retry and Resource Management

## Objective

Learn and implement decorators, retry logic, and context managers for reliable ML pipeline execution.

## 1. @timeit

The `@timeit` decorator measures how long a function takes to execute.

It is applied to `Pipeline.run()` to measure the pipeline execution time.

## 2. @retry

The `@retry(max_attempts=3)` decorator retries a function when an exception occurs.

In the pipeline, a failed execution is attempted up to 3 times before the final exception is raised.

## 3. Context Manager

`ResourceManager` uses `__enter__()` and `__exit__()` to manage a resource.

The resource is released even when an exception occurs inside the `with` block.

## 4. Pipeline Integration

The pipeline uses:

- `@timeit`
- `@retry(max_attempts=3)`
- `ResourceManager`

This provides execution timing, retry handling, and resource cleanup.

## 5. Exception Test

A temporary `ValueError` was introduced in a pipeline step.

The test confirmed:

- The pipeline retried 3 times.
- The resource was released after every failed attempt.
- The final exception was propagated correctly.

## Result

Day 5 successfully demonstrated decorators, retry logic, context managers, and exception-safe resource management in the ML pipeline.