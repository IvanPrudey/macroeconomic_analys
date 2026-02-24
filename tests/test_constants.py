from constants import (
    AVAILABLE_REPORTS,
    DATA_FOLDER,
    EXPECTED_HEADERS,
    SOME_TEST_DATA,
)
from reports.using_reports import AverageGdpReport


class TestAvailableReportsConstant:

    def test_available_reports_is_dict(self):
        assert isinstance(AVAILABLE_REPORTS, dict)

    def test_available_reports_not_empty(self):
        assert len(AVAILABLE_REPORTS) > 0

    def test_average_gdp_exist(self):
        assert 'average-gdp' in AVAILABLE_REPORTS.keys()
        assert AVAILABLE_REPORTS['average-gdp'] == AverageGdpReport


class TestDataFolderConstant:

    def test_data_folder_is_str(self):
        assert isinstance(DATA_FOLDER, str)

    def test_data_folder_not_empty(self):
        assert DATA_FOLDER != ''


class TestExpectedHeadersConstant:

    def test_expected_headers_is_str(self):
        assert isinstance(EXPECTED_HEADERS, str)

    def test_expected_headers_not_empty(self):
        assert EXPECTED_HEADERS != ''

    def test_correct_headers(self):
        assert EXPECTED_HEADERS == (
            'country,year,gdp,gdp_growth,inflation,'
            'unemployment,population,continent'
        )


class TestSomeTestDataConstant:

    def test_some_test_data_is_list(self):
        assert isinstance(SOME_TEST_DATA, list)

    def test_each_item_is_dict(self):
        for item in SOME_TEST_DATA:
            assert isinstance(item, dict)

    def test_some_test_data_not_empty(self):
        assert len(SOME_TEST_DATA) > 0

    def test_correct_expected_headers(self):
        expected_keys = set(EXPECTED_HEADERS.split(','))
        for item in SOME_TEST_DATA:
            assert set(item.keys()) == expected_keys
