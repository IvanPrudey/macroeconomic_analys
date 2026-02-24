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
SOME_TEST_DATA = [
    {
        'country': 'Russia',
        'year': 2023,
        'gdp': 18600.0,
        'gdp_growth': 2.1,
        'inflation': 5.9,
        'unemployment': 3.2,
        'population': 144,
        'continent': 'Eurasia'
    },
    {
        'country': 'Russia',
        'year': 2022,
        'gdp': 17900,
        'gdp_growth': -2.1,
        'inflation': 11.9,
        'unemployment': 3.8,
        'population': 144,
        'continent': 'Eurasia'
    },
    {
        'country': 'Belarus',
        'year': 2023,
        'gdp': 2200,
        'gdp_growth': 3.1,
        'inflation': 5.0,
        'unemployment': 3.5,
        'population': 9,
        'continent': 'Europe'
    },
    {
        'country': 'Belarus',
        'year': 2022,
        'gdp': 2100,
        'gdp_growth': -4.2,
        'inflation': 12.8,
        'unemployment': 3.9,
        'population': 9,
        'continent': 'Europe'
    },
    {
        'country': 'China',
        'year': 2023,
        'gdp': 17963,
        'gdp_growth': 5.2,
        'inflation': 2.5,
        'unemployment': 5.2,
        'population': 1425,
        'continent': 'Asia'
    },
    {
        'country': 'China',
        'year': 2022,
        'gdp': 17734,
        'gdp_growth': 3.0,
        'inflation': 2.0,
        'unemployment': 5.6,
        'population': 1423,
        'continent': 'Asia'
    },
]
