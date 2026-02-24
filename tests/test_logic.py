import os
import pytest
from main import (
    verify_csv_headers,
    load_data_from_csv_files,
    parse_arguments,
)

from reports.using_reports import AverageGdpReport

TEST_COUNT_ROWS_OF_TWO_FILES = 7
TEST_AVG_GDP_OF_RUSSIA = 18250
COUNT_FIELDS_IN_AVG_GDP_REPORT = 2


class TestVerifyCsvHeaders:

    def test_valid_headers_returns_true(
            self,
            temp_csv_with_correct_headers_without_data,
            expected_headers_string
    ):
        result = verify_csv_headers(
            temp_csv_with_correct_headers_without_data,
            expected_headers_string
        )
        assert result is True

    def test_invalid_headers_returns_false(
            self,
            temp_csv_with_invalid_headers_without_data,
            expected_headers_string
    ):
        result = verify_csv_headers(
            temp_csv_with_invalid_headers_without_data,
            expected_headers_string
        )
        assert result is False

    def test_empty_file_returns_false(
            self,
            temp_empty_csv_file,
            expected_headers_string
    ):
        result = verify_csv_headers(
            temp_empty_csv_file,
            expected_headers_string
        )
        assert result is False


class TestLoadDataFromCsvFiles:

    def test_load_one_file(
            self,
            temp_csv_with_test_data,
            expected_headers_string,
            correct_some_test_data
    ):
        folder = os.path.dirname(temp_csv_with_test_data)
        filename = os.path.basename(temp_csv_with_test_data)
        result = load_data_from_csv_files(
            [filename],
            folder,
            expected_headers_string
        )
        assert isinstance(result, list)
        assert len(result) == len(correct_some_test_data)
        assert result[0]['country'] == 'Russia'

    def test_load_two_files(
            self,
            temp_csv_with_test_data,
            temp_csv_with_one_row_data,
            expected_headers_string
    ):
        folder = os.path.dirname(temp_csv_with_test_data)
        filename_1 = os.path.basename(temp_csv_with_test_data)
        filename_2 = os.path.basename(temp_csv_with_one_row_data)
        result = load_data_from_csv_files(
            [filename_1, filename_2],
            folder,
            expected_headers_string
        )
        assert len(result) == TEST_COUNT_ROWS_OF_TWO_FILES

    def test_file_not_exits(self, expected_headers_string):
        folder = 'some_folder'
        filename = 'some_file.csv'
        with pytest.raises(SystemExit):
            load_data_from_csv_files(
                [filename],
                folder,
                expected_headers_string
            )


class TestAverageGdpReport:
    def test_report_name(self):
        report = AverageGdpReport()
        assert report.name == 'average-gdp'

    def test_report_headers(self):
        report = AverageGdpReport()
        assert report.headers == ['country', 'gdp']

    def test_calculate_returns_list(self, correct_some_test_data):
        report = AverageGdpReport()
        result = report.calculate(correct_some_test_data)
        assert isinstance(result, list)

    def test_calculate_returns_elements_with_correct_keys(
            self,
            correct_some_test_data
    ):
        report = AverageGdpReport()
        result = report.calculate(correct_some_test_data)
        for item in result:
            assert isinstance(item, dict)
            assert 'country' in item
            assert 'gdp' in item
            assert len(item) == COUNT_FIELDS_IN_AVG_GDP_REPORT

    def test_average_calculation_for_russia(self, correct_some_test_data):
        report = AverageGdpReport()
        result = report.calculate(correct_some_test_data)
        russia_item = None
        for item in result:
            if item['country'] == 'Russia':
                russia_item = item
                break
        assert russia_item is not None
        assert russia_item['gdp'] == TEST_AVG_GDP_OF_RUSSIA


class TestPrintReport:
    pass


class TestParseArguments:

    def test_correct_arguments(self, available_reports_sample, monkeypatch):
        test_args = [
            'main.py',
            '--files',
            'example.csv',
            '--report',
            'average-gdp'
        ]
        monkeypatch.setattr('sys.argv', test_args)
        files, report = parse_arguments(available_reports_sample)
        assert files == ['example.csv']
        assert report == 'average-gdp'

    def test_without_files_arg(self, available_reports_sample, monkeypatch):
        test_args = ['main.py', '--report', 'average-gdp']
        monkeypatch.setattr('sys.argv', test_args)
        with pytest.raises(SystemExit) as excinfo:
            parse_arguments(available_reports_sample)
        assert excinfo.value.code == 2

    def test_without_report_arg(self, available_reports_sample, monkeypatch):
        test_args = ['main.py', '--files', 'data.csv']
        monkeypatch.setattr('sys.argv', test_args)
        with pytest.raises(SystemExit) as excinfo:
            parse_arguments(available_reports_sample)
        assert excinfo.value.code == 2
