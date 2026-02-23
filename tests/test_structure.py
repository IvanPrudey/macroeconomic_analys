class TestProjectStructure:

    def test_data_folder_exists(self, data_dir):
        assert data_dir.exists()
        assert data_dir.is_dir()

    def test_data_folder_contains_csv(self, data_dir):
        csv_files = list(data_dir.glob('*.csv'))
        assert len(csv_files) > 0

    def test_reports_package_exists(self, reports_dir):
        assert reports_dir.exists()
        assert reports_dir.is_dir()
        assert (reports_dir / '__init__.py').exists()

    def test_base_report_exists(self, reports_dir):
        assert (reports_dir / 'base_report.py').exists()

    def test_using_reports_exists(self, reports_dir):
        assert (reports_dir / 'using_reports.py').exists()

    def test_constants_exists(self, project_root):
        assert (project_root / 'constants.py').exists()

    def test_requirements_exists(self, project_root):
        assert (project_root / 'requirements.txt').exists()

    def test_main_exists(self, project_root):
        assert (project_root / 'main.py').exists()
