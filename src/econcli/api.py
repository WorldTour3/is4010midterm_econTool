"""Handles all external API calls."""

import requests

REST_COUNTRIES_API_URL = "https://restcountries.com/v3.1"



def get_country_info(country_name):
    """Fetches general country information from the REST Countries API."""
    try:
        response = requests.get(f"{REST_COUNTRIES_API_URL}/name/{country_name}")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data[0]
    except (requests.RequestException, IndexError):
        return None

def get_all_countries():
    """Fetches a list of all countries."""
    try:
        response = requests.get(f"{REST_COUNTRIES_API_URL}/all?fields=name")
        response.raise_for_status()
        data = response.json()
        return sorted([country['name']['common'] for country in data])
    except requests.RequestException:
        return []

def get_gdp_per_capita(country_code):
    """Fetches GDP per capita from the World Bank API."""
    if not country_code: return None
    try:
        url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.PCAP.CD?format=json&date=2022"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Data is in the second element of the top-level array
        if len(data) > 1 and data[1]:
            return float(data[1][0]['value'])
        return None
    except (requests.RequestException, KeyError, IndexError, TypeError):
        return None

def get_inflation_rate(country_code):
    """Fetches inflation from the World Bank API."""
    if not country_code: return None
    try:
        url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/FP.CPI.TOTL.ZG?format=json&date=2022"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if len(data) > 1 and data[1]:
            return float(data[1][0]['value'])
        return None
    except (requests.RequestException, KeyError, IndexError, TypeError):
        return None
