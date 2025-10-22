"""Tests for the commands.py module."""

import pytest
from unittest.mock import patch
from econcli import commands

@patch('econcli.api.get_country_info')
@patch('econcli.api.get_gdp_per_capita')
@patch('econcli.api.get_inflation_rate')
def test_handle_country_command_success(mock_get_inflation, mock_get_gdp, mock_get_info, capsys):
    """Test the country command with a valid country."""
    mock_get_info.return_value = {
        'name': {'common': 'Testland'},
        'cca3': 'TSL',
        'flag': '🇹🇸',
        'population': 1234567,
        'region': 'Test Region',
        'currencies': {'TSD': {'name': 'Test Dollar'}}
    }
    mock_get_gdp.return_value = 55000
    mock_get_inflation.return_value = 3.5

    commands.handle_country_command('Testland')
    captured = capsys.readouterr()
    
    assert "🇹🇸 Testland" in captured.out
    assert "GDP (per capita): $55,000" in captured.out
    assert "Inflation rate: 3.5%" in captured.out
    assert "Population: 1,234,567" in captured.out

@patch('econcli.api.get_country_info')
def test_handle_country_command_not_found(mock_get_info, capsys):
    """Test the country command with an invalid country."""
    mock_get_info.return_value = None
    commands.handle_country_command('Fakeland')
    captured = capsys.readouterr()
    assert "Could not find information for 'Fakeland'" in captured.out

@patch('econcli.api.get_country_info')
@patch('econcli.api.get_gdp_per_capita')
@patch('econcli.api.get_inflation_rate')
def test_handle_compare_command(mock_get_inflation, mock_get_gdp, mock_get_info, capsys):
    """Test the compare command."""
    # Configure mock for two different countries
    mock_get_info.side_effect = [
        {'name': {'common': 'CountryA'}, 'cca3': 'CTA'},
        {'name': {'common': 'CountryB'}, 'cca3': 'CTB'}
    ]
    mock_get_gdp.side_effect = [80000, 75000]
    mock_get_inflation.side_effect = [1.5, 2.5]

    commands.handle_compare_command('CountryA', 'CountryB')
    captured = capsys.readouterr()

    assert "Comparing Countrya vs. Countryb" in captured.out
    assert "| GDP (per capita)  | $80,000         | $75,000         |" in captured.out
    assert "| Inflation Rate    | 1.5%            | 2.5%            |" in captured.out
