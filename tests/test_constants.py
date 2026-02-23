from constants import AVAILABLE_REPORTS, DATA_FOLDER, EXPECTED_HEADERS


class TestAvailableReportsConstant:

    def test_available_reports_is_dict(self):
        assert isinstance(AVAILABLE_REPORTS, dict)


class TestDataFolderConstant:

    def test_data_folder_is_str(self):
        assert isinstance(DATA_FOLDER, str)


class TestExpectedHeadersConstant:

    def test_expected_headers_is_str(self):
        assert isinstance(EXPECTED_HEADERS, str)
