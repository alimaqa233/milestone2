# Diabetes Dataset Analysis & Data Cleaning

This repository contains Python scripts for loading, exploring, and cleaning the Diabetes Dataset.

## Features
- Inspects dataset dimensions, column names, missing values, and invalid zero values.
- Replaces invalid zero values in clinical columns (`Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`) with the median.
- Deduplicates rows and saves the cleaned dataset to `diabetes_clean.csv`.

## Setup & Execution
```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run script
python main.py
```
