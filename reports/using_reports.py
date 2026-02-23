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

        def get_gdp(item):
            return item['gdp']

        country_gdp_sum = {}
        country_count = {}
        for row in data:
            country = row['country']
            gdp = row['gdp']
            if country not in country_gdp_sum:
                country_gdp_sum[country] = 0
                country_count[country] = 0
            country_gdp_sum[country] += gdp
            country_count[country] += 1
        result = []
        for country in country_gdp_sum:
            avg_gdp = country_gdp_sum[country] / country_count[country]
            result.append(
                {
                    'country': country,
                    'gdp': round(avg_gdp)
                }
            )
        result.sort(key=get_gdp, reverse=True)
        return result


class SomeReport(Report):

    @property
    def name(self) -> str:
        return 'some'

    @property
    def headers(self) -> List[str]:
        return ['country', 'year', 'population']

    def calculate(
            self, data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        calculated_data = data
        return calculated_data
