A simple Python script to clean messy CSV data using pandas.
# 🧹 Data Cleaning Automation

A simple Python script that reads raw CSV data, cleans it, and outputs a processed version.  
Perfect for preparing data for analysis or reporting.

## 🔧 Features
- Removes duplicate rows
- Fills missing numeric values with the median
- Cleans column names (lowercase, replaces spaces with underscores)
- (Optional) Converts date columns to datetime
- Saves the cleaned dataset as `cleaned_data.csv`

## 📂 Files
- `clean_data.py`: the cleaning script
- `sample_data.csv`: placeholder file to test cleaning

## ▶️ Usage
```bash
python clean_data.py
