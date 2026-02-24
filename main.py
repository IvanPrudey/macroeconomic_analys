import argparse
import csv
import os
import sys

from tabulate import tabulate

from constants import (
    AVAILABLE_REPORTS,
    DATA_FOLDER,
    EXPECTED_HEADERS,
)

MSG_HELP_1 = (
    'Перечень .csv файлов для анализа '
    '(можно указать несколько через пробел)'
)
MSG_HELP_2 = 'Доступные варианты отчетов'
MSG_INFO_1 = 'заголовки НЕ соответствуют, пропускаем'


def parse_arguments(available_reports):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help=MSG_HELP_1
    )
    parser.add_argument(
        '--report',
        required=True,
        choices=list(available_reports.keys()),
        help=f'{MSG_HELP_2}: {", ".join(available_reports.keys())}'
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


def load_data_from_csv_files(
        data_files_pathes, full_path_data_folder, expected_headers
):
    full_massive_data = []
    for file_path in data_files_pathes:
        full_file_path = os.path.join(full_path_data_folder, file_path)
        if not os.path.exists(full_file_path):
            print(f'Файл {full_file_path} отсутствует')
            sys.exit(1)
        if verify_csv_headers(full_file_path, expected_headers):
            print(f'{full_file_path} - заголовки корректны')
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
            print(f'Файл {full_file_path} - {MSG_INFO_1}')
    return full_massive_data


def print_report(report_data, headers):
    if not report_data:
        print('Данные для вывода отсутствуют')
        return
    table_data = []
    for i, row in enumerate(report_data, 1):
        row_values = [row[header] for header in headers]
        table_data.append([i] + row_values)
    display_headers = [''] + headers
    print(tabulate(
        table_data,
        headers=display_headers,
        tablefmt='grid',
        floatfmt='.2f'
    ))


def main():
    try:
        console_files, console_report_name = parse_arguments(AVAILABLE_REPORTS)
    except Exception as e:
        print(f'Ошибка при разборе аргументов командной строки: {e}')
        sys.exit(1)

    if console_report_name not in AVAILABLE_REPORTS.keys():
        print(f'Отчета с именем {console_report_name} нет в списке доступных')
        print(f'Доступные отчеты: {", ".join(AVAILABLE_REPORTS.keys())}')
        sys.exit(1)
    print(f'Старт отчета: {console_report_name}')
    print(f'Файлы для анализа: {console_files}')
    full_path_data = os.path.abspath(DATA_FOLDER)
    full_massive_data = load_data_from_csv_files(
        console_files, full_path_data, EXPECTED_HEADERS
    )

    if not full_massive_data:
        print('Нет данных для анализа')
        sys.exit(1)
    print(f'Загружено {len(full_massive_data)} записей!')

    try:
        report_class = AVAILABLE_REPORTS[console_report_name]
        report = report_class()
        report_data = report.calculate(full_massive_data)
    except KeyError as e:
        print(f'Ошибка: класс отчета не найден - {e}')
        sys.exit(1)
    except Exception as e:
        print(f'Непредвиденная ошибка при расчетах: {e}')
        sys.exit(1)
    try:
        print(f'------{report.name}--{", ".join(console_files)}------')
        print_report(report_data, report.headers)
    except Exception as e:
        print(f'Ошибка при выводе отчета: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
