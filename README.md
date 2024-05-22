# File Processor

## Objective
The File Processor is designed to efficiently handle .dat files, remove duplicate rows based on the 'id' column, and generate CSV files with a footer containing salary information.

## Components
- Input Module: Reads .dat files from the designated input folder.
- Data Processor: Processes and modifies the data as required.
- Duplicate Checker: Removes duplicate rows based on the 'id' column.
- CSV Writer: Writes the processed data to CSV files.
- Footer Generator: Adds a footer to the CSV files with salary information.

## Workflow
1. **Input:** The Input Module reads .dat files from the input folder.
2. **Processing:** The Data Processor modifies the data, removes duplicates, and calculates salaries.
3. **Output:** The CSV Writer writes the processed data to CSV files with the footer containing salary information.

## Features
- Handles .dat file format efficiently.
- Removes duplicate rows based on the 'id' column to ensure data integrity.
- Generates CSV files with a footer that includes salary information for each processed dataset.

## Technologies Used
- Python programming language
- CSV module for CSV file handling

## Deployment
The File Processor can be deployed and run on any system with Python installed.
