import os
import csv
from typing import List, Tuple

def read_dat_file(file_path: str) -> List[List[str]]:
    """
    Read data from a .dat file and return as a list of lists.
    
    Args:
    - file_path (str): Path to the .dat file.
    
    Returns:
    - List[List[str]]: List of lists representing the data read from the file.
    """
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            if len(columns) >= 7:
                job_title = ' '.join(columns[4:-2])
                modified_row = columns[:4] + [job_title] + columns[-2:]
                data.append(modified_row)
    return data

def remove_duplicates(data: List[List[str]]) -> List[List[str]]:
    """
    Remove duplicate rows based on 'id' column.
    
    Args:
    - data (List[List[str]]): Input data as a list of lists.
    
    Returns:
    - List[List[str]]: Data with duplicate rows removed.
    """
    seen_ids = set()
    unique_data = []
    for row in data:
        if row[0] not in seen_ids:
            seen_ids.add(row[0])
            unique_data.append(row)
    return unique_data

def write_to_csv(data: List[List[str]], output_file_path: str, headers: List[str], second_highest_salary: int, average_salary: float):
    """
    Write the processed data to a CSV file with a footer.
    
    Args:
    - data (List[List[str]]): Processed data as a list of lists.
    - output_file_path (str): Path to the output CSV file.
    - headers (List[str]): Headers for the CSV file.
    - second_highest_salary (int): Second highest salary value.
    - average_salary (float): Average salary value.
    """
    with open(output_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(data)
        writer.writerow([])
        writer.writerow([f'Second Highest Salary = {second_highest_salary}', f'Average Salary = {average_salary}'])

def process_files(input_folder: str, output_folder: str):
    """
    Process all .dat files in the input folder and write the result to CSV files in the output folder.
    
    Args:
    - input_folder (str): Path to the input folder containing .dat files.
    - output_folder (str): Path to the output folder where CSV files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.dat'):
            file_path = os.path.join(input_folder, file_name)
            data = read_dat_file(file_path)
            headers = data[0] if data else []
            if headers and headers[0] == 'id':
                data = remove_duplicates(data[1:])
                salaries = [int(row[-2]) for row in data]
                salaries.sort(reverse=True)
                second_highest_salary = salaries[1]
                average_salary = sum(salaries) / len(salaries)
                rounded_average = round(average_salary, 2)
                output_file_name = f"{os.path.splitext(file_name)[0]}.csv"
                output_file_path = os.path.join(output_folder, output_file_name)
                write_to_csv(data, output_file_path, headers, second_highest_salary, rounded_average)
                print(f"Processed {file_name} and saved to {output_file_path}")

input_folder = 'path to input_folder .dat files'
output_folder = 'path to output_folder'
process_files(input_folder, output_folder)
