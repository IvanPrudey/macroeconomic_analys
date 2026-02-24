import pytest
from pathlib import Path

from constants import DATA_FOLDER, SOME_TEST_DATA


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

