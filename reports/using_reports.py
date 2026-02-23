from typing import List, Dict, Any

from reports.base_report import Report


class AverageGdpReport(Report):

    @property
    def name(self) -> str:
        return 'average-gdp'

    @property
    def headers(self) -> List[str]:
        return ['country', 'gdp']

    def calculate(
            self, data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        calculated_data = data
        return calculated_data


class SomeReport(Report):

    @property
    def name(self) -> str:
        return 'some'

    @property
    def headers(self) -> List[str]:
        return ['some_1', 'some_2']

    def calculate(
            self, data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        return f'Результат {self.name} отчета со столбцами {self.headers}'
