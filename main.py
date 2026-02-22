import argparse
import csv
import os
import sys

from tabulate import tabulate

from constants import (
    AVAILABLE_REPORTS,
    EXPECTED_HEADERS,
    DATA_FOLDER,
)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Перечень .csv файлов для анализа(можно указать несколько через пробел)'
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=list(AVAILABLE_REPORTS.keys()),
        help=f"Доступные варианты отчетов {', '.join(AVAILABLE_REPORTS.keys())}"
    )
    parse_args = parser.parse_args()
    return parse_args.files, parse_args.report


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


# def create_list_of_files_csv(data_folder):
#     data_files_name_list = []
#     if os.path.exists(data_folder):
#         for filename in os.listdir(data_folder):
#             file_path = os.path.join(data_folder, filename)
#             if os.path.isfile(file_path) and filename.endswith('.csv'):
#                 data_files_name_list.append(filename)
#         return data_files_name_list
#     else:
#         print(f'Папка {data_folder} не существует')
#         return data_files_name_list


def load_data_from_csv_files(
        data_files_pathes, full_path_data, expected_headers
):
    full_massive_data = []
    for file_path in data_files_pathes:
        full_file_path = '/'.join([full_path_data, file_path])
        if not os.path.exists(full_file_path):
            print(f'Файл {full_file_path} отсутствует')
            sys.exit(1)
        if verify_csv_headers(full_file_path, expected_headers):
            print(f'{full_file_path} - заголовки корректны, стартуем загрузку даных')
            try:
                with open(full_file_path, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        loading_row = {
                            'country': row['country'],
                            'year': int(row['year']),
                            'gdp': float(row['gdp']),
                            'gdp_growth': float(row['gdp_growth']),
                            'inflation': float(row['inflation']),
                            'unemployment': float(row['unemployment']),
                            'population': int(row['population']),
                            'continent': row['continent']
                        }
                        full_massive_data.append(loading_row)
            except Exception as e:
                print(f'Ошибка при загрузке данных из {full_file_path}: {e}')
                sys.exit(1)
        else:
            print(f'Файл {full_file_path} - заголовки НЕ соответствуют, пропускаем')
    return full_massive_data


def print_report(massive_data_list):
    if not massive_data_list:
        print('Данные для вывода отсутствуют')
        return
    headers_of_table = list(massive_data_list[0].keys())
    table_data = []
    for i, row in enumerate(massive_data_list, 1):
        row_values = [row[key] for key in headers_of_table]
        table_data.append([i] + row_values)
        display_headers = [''] + headers_of_table
    print(tabulate(table_data, headers=display_headers, tablefmt='grid'))


def main():
    console_files, console_report_name = parse_arguments()
    print(f'Старт отчета: {console_report_name}')
    print(f'Файлы для анализа: {console_files}')
    print('--------------111---------------')
    full_path_data = os.path.abspath(DATA_FOLDER)
    print(full_path_data)
    print('--------------222---------------')
    full_massive_data = load_data_from_csv_files(
        console_files, full_path_data, EXPECTED_HEADERS
    )
    
    if not full_massive_data:
        print('Нет данных для анализа')
        sys.exit(1)
    print(f'Загружено {len(full_massive_data)} записей!')
    # print_report(full_massive_data)


if __name__ == '__main__':
    main()
