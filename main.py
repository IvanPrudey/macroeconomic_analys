import csv
import os
from pathlib import Path

from constants import EXPECTED_HEADERS


def verify_csv_headers(file_path, expected_headers_str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            actual_headers = next(reader)
            actual_headers_str = ','.join(actual_headers)
            return actual_headers_str == expected_headers_str
    except Exception as e:
        print(f'Ошибка при чтении файла {file_path}: {e}')
        return False


def main():
    data_folder = 'data'
    full_path_data = os.path.abspath(data_folder)
    data_files_name_list = []
    if os.path.exists(data_folder):
        for filename in os.listdir(data_folder):
            file_path = os.path.join(data_folder, filename)
            if os.path.isfile(file_path) and filename.endswith('.csv'):
                data_files_name_list.append(filename)
        print(f'список файлов в папке {full_path_data} - {data_files_name_list}')


if __name__ == '__main__':
    main()
