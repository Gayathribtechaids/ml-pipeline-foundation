# Day 2 — Iterators, Generators & Memory-Efficient Data Handling

## Objective

Implement a memory-efficient image batch iterator that processes images in fixed-size batches instead of loading the complete dataset into memory.

## Implementation

Created `ImageBatchIterator` using Python's iterator protocol:

- `__iter__()` returns the iterator.
- `__next__()` retrieves the next batch.
- `Path.glob()` provides image paths lazily.
- Pillow loads only the images required for the current batch.
- `batch_size` validation prevents invalid batch sizes.

## Memory Testing

Memory usage was measured using Python's `tracemalloc` module.

Batch size used:

```text
10 images