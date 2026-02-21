import csv
import os
import sys

from constants import EXPECTED_HEADERS, DATA_FOLDER


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


def create_list_of_files_csv(data_folder):
    data_files_name_list = []
    if os.path.exists(data_folder):
        for filename in os.listdir(data_folder):
            file_path = os.path.join(data_folder, filename)
            if os.path.isfile(file_path) and filename.endswith('.csv'):
                data_files_name_list.append(filename)
        return data_files_name_list
    else:
        print(f'Папка {data_folder} не существует')
        return data_files_name_list


def main():
    full_path_data = os.path.abspath(DATA_FOLDER)
    data_files_name_list = create_list_of_files_csv(DATA_FOLDER)
    if not data_files_name_list:
        print('Нет файлов данных .csv для обработки. Программа завершена')
        sys.exit(1)
    print(f'список файлов в папке data/ {data_files_name_list}')


if __name__ == '__main__':
    main()
