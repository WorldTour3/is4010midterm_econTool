"""Tests for the api.py module."""

import pytest
from unittest.mock import patch
from econcli import api

@pytest.fixture
def mock_requests_get():
    """Fixture to mock requests.get."""
    with patch('econcli.api.requests.get') as mock_get:
        yield mock_get

def test_get_country_info_success(mock_requests_get):
    """Test successful fetching of country info."""
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [{
        'name': {'common': 'Testland'},
        'cca3': 'TSL',
        'population': 1000000,
        'region': 'Test Region',
        'currencies': {'TSD': {'name': 'Test Dollar'}}
    }]

    info = api.get_country_info('Testland')
    assert info is not None
    assert info['name']['common'] == 'Testland'

def test_get_country_info_failure(mock_requests_get):
    """Test failure in fetching country info."""
    mock_requests_get.side_effect = api.requests.RequestException
    info = api.get_country_info('FailLand')
    assert info is None

def test_get_gdp_per_capita_success(mock_requests_get):
    """Test successful fetching of GDP."""
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {'page': 1, 'pages': 1},
        [{ 'value': 50000.0 }]
    ]

    gdp = api.get_gdp_per_capita('USA')
    assert gdp == 50000.0

def test_get_inflation_rate_missing_country(mock_requests_get):
    """Test fetching inflation for a missing country."""
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [None, None]

    inflation = api.get_inflation_rate('MEX') # Different country
    assert inflation is None
