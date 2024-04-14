@echo off
set /p data_source="Enter the data source (csv/excel): "
set /p output_format="Enter the desired output format (csv/excel): "
python generate_data_reports.py %data_source% %output_format%
pause