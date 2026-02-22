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
        return f'Результат работы среднего ВПП по стране'
