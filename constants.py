from reports.using_reports import AverageGdpReport, SomeReport

EXPECTED_HEADERS = (
    'country,year,gdp,gdp_growth,inflation,'
    'unemployment,population,continent'
)
DATA_FOLDER = 'data'
AVAILABLE_REPORTS = {
    'average-gdp': AverageGdpReport,
    'some': SomeReport,
}
