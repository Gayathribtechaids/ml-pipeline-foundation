# ML Pipeline Foundation

A production-style Python project focused on building a modular, reproducible, and memory-efficient machine learning pipeline.

## Project Status

Day 1 - Environment Architecture & Repository Foundation

The application logic will be developed incrementally as part of the project learning tasks.

## Requirements

* Python 3.10 or higher
* Git

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ml-pipeline-foundation
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the project

```bash
pip install -e .
```

## Project Structure

```text
ml-pipeline-foundation/
│
├── src/
│   └── ml_pipeline/
│       └── __init__.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── configs/
├── scripts/
├── tests/
│
├── .gitignore
├── pyproject.toml
└── README.md
```

## Purpose of Each Directory

* `src/` - Main Python source code
* `data/raw/` - Original input data
* `data/processed/` - Processed data
* `notebooks/` - Experiments and analysis
* `configs/` - Project configuration files
* `scripts/` - Utility and execution scripts
* `tests/` - Automated tests
