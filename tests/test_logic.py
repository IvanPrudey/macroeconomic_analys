from main import verify_csv_headers


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
