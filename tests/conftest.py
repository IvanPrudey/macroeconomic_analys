import csv
import os
import pytest
import tempfile
from pathlib import Path

from constants import DATA_FOLDER, EXPECTED_HEADERS, SOME_TEST_DATA


@pytest.fixture
def project_root():
    return Path(__file__).parent.parent


@pytest.fixture
def data_dir(project_root):
    return project_root / DATA_FOLDER


@pytest.fixture
def reports_dir(project_root):
    return project_root / 'reports'


@pytest.fixture
def csv_files(data_dir):
    return list(data_dir.glob('*.csv'))


@pytest.fixture
def correct_some_test_data():
    return SOME_TEST_DATA.copy()


@pytest.fixture
def expected_headers_list():
    return EXPECTED_HEADERS.split(',')


@pytest.fixture
def temp_csv_with_correct_headers_without_data(expected_headers_list):
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as f:
        writer = csv.writer(f)
        writer.writerow(expected_headers_list)
        temp_file = f.name
    yield temp_file
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def temp_csv_with_invalid_headers_without_data():
    invalid_headers = ['city', 'month', 'count']
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as f:
        writer = csv.writer(f)
        writer.writerow(invalid_headers)
        temp_file = f.name
    yield temp_file
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def temp_empty_csv_file():
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as f:
        f.write('')
        temp_file = f.name
    yield temp_file
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def temp_csv_with_test_data(correct_some_test_data, expected_headers_list):
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.csv',
        delete=False,
        encoding='utf-8'
    ) as f:
        writer = csv.writer(f)
        writer.writerow(expected_headers_list)
        for row in correct_some_test_data:
            writer.writerow([
                row['country'],
                row['year'],
                row['gdp'],
                row['gdp_growth'],
                row['inflation'],
                row['unemployment'],
                row['population'],
                row['continent']
            ])
        temp_file = f.name
    yield temp_file
    if os.path.exists(temp_file):
        os.unlink(temp_file)
