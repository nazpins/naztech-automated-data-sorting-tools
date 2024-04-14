import pandas as pd

def generate_report(data_source, output_format):
    if data_source == 'csv':
        file_path = input("Enter the path to the CSV file: ")
        data = pd.read_csv(file_path)
    elif data_source == 'excel':
        file_path = input("Enter the path to the Excel file: ")
        sheet_name = input("Enter the sheet name: ")
        data = pd.read_excel(file_path, sheet_name=sheet_name)
    else:
        print("Unsupported data source. Please provide a CSV or Excel file.")
        return

    if output_format == 'csv':
        output_path = input("Enter the output file path: ")
        data.to_csv(output_path, index=False)
        print("Report generated successfully.")
    elif output_format == 'excel':
        output_path = input("Enter the output file path: ")
        data.to_excel(output_path, index=False)
        print("Report generated successfully.")
    else:
        print("Unsupported output format. Please choose 'csv' or 'excel'.")

if __name__ == '__main__':
    data_source = input("Enter the data source (csv/excel): ")
    output_format = input("Enter the desired output format (csv/excel): ")
    generate_report(data_source, output_format)