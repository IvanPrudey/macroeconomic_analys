import os
from main import (
    verify_csv_headers,
    load_data_from_csv_files,
)


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
