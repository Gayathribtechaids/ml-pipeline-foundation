# Day 7 — Structured Logging

## Objective

Replace simple `print()` statements with Python's logging system.

## Logging Levels

The project logger uses:

- INFO — normal pipeline activity
- WARNING — unexpected but recoverable situations
- ERROR — failures

## Logger Configuration

A central logger was created using Python's `logging` module.

The logger includes:

- Timestamp
- Log level
- Log message

Logs are sent to both the console and `pipeline.log`.

## Pipeline Integration

The pipeline processing steps use `logger.info()` instead of `print()`.

The following steps were updated:

- Loading images
- Resizing images
- Converting images to grayscale

## File Logging

Pipeline logs are written to `pipeline.log`.

The log file is added to `.gitignore` so generated logs are not committed to Git.

## Testing

The logger was tested with INFO, WARNING, and ERROR messages.

The pipeline was also executed to verify that structured logs appear in both the terminal and log file.

## Result

Day 7 successfully implemented structured logging and integrated it into the ML pipeline.