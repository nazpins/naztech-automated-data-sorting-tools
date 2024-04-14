import pandas as pd
import os

def merge_csv_files(file_list, output_file):
    merged_data = pd.concat([pd.read_csv(file) for file in file_list])
    merged_data.to_csv(output_file, index=False)
    print("CSV files merged successfully.")

if __name__ == '__main__':
    file_list = []
    while True:
        file_path = input("Enter the path to a CSV file (or press Enter to finish): ")
        if file_path == '':
            break
        file_list.append(file_path)
    output_file = input("Enter the output file path: ")
    merge_csv_files(file_list, output_file)