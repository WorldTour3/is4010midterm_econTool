"""Implements the logic for each CLI command."""

from . import api, utils

def handle_country_command(country_name):
    """Handles the 'country' command."""
    info = api.get_country_info(country_name)
    if not info:
        print(f"Could not find information for '{country_name}'.")
        return

    country_code = info.get('cca3')
    gdp = api.get_gdp_per_capita(country_code)
    inflation = api.get_inflation_rate(country_code)

    flag = info.get('flag', '')
    name = info.get('name', {}).get('common', 'N/A')
    population = info.get('population')
    region = info.get('region', 'N/A')
    currency_data = info.get('currencies', {})

    if currency_data:
        currency_code = next(iter(currency_data.keys()), 'N/A')
        currency_name = currency_data.get(currency_code, {}).get('name', 'N/A')
    else:
        currency_code = 'N/A'
        currency_name = 'N/A'

    print(f"{flag} {name}")
    print(f"GDP (per capita): {utils.format_currency(gdp)}")
    print(f"Inflation rate: {utils.format_percentage(inflation)}")
    print(f"Population: {utils.format_population(population)}")
    print(f"Currency: {currency_name} ({currency_code})")
    print(f"Region: {region}")

def handle_compare_command(country1_name, country2_name):
    """Handles the 'compare' command."""
    print(f"Comparing {country1_name.title()} vs. {country2_name.title()}\n")

    info1 = api.get_country_info(country1_name)
    info2 = api.get_country_info(country2_name)

    if not info1 or not info2:
        if not info1:
            print(f"Could not find information for '{country1_name}'.")
        if not info2:
            print(f"Could not find information for '{country2_name}'.")
        return

    gdp1 = api.get_gdp_per_capita(info1.get('cca3'))
    gdp2 = api.get_gdp_per_capita(info2.get('cca3'))
    inflation1 = api.get_inflation_rate(info1.get('cca3'))
    inflation2 = api.get_inflation_rate(info2.get('cca3'))

    # Create and print a formatted table
    header = f"| {'Metric':<15} | {info1['name']['common']:<15} | {info2['name']['common']:<15} |"
    separator = f"|{'-'*17}|{'-'*17}|{'-'*17}|"
    gdp_row = f"| {'GDP (per capita)':<15} | {utils.format_currency(gdp1):<15} | {utils.format_currency(gdp2):<15} |"
    inf_row = f"| {'Inflation Rate':<15} | {utils.format_percentage(inflation1):<15} | {utils.format_percentage(inflation2):<15} |"

    print(header)
    print(separator)
    print(gdp_row)
    print(inf_row)

def handle_currency_command(country_name):
    """Handles the 'currency' command."""
    info = api.get_country_info(country_name)
    if not info:
        print(f"Could not find information for '{country_name}'.")
        return

    currency_data = info.get('currencies', {})
    if not currency_data:
        print(f"No currency information found for {country_name}.")
        return

    currency_code = next(iter(currency_data.keys()))
    currency_name = currency_data[currency_code].get('name', 'N/A')
    
    print(f"{currency_name} ({currency_code})")

def handle_list_command():
    """Handles the 'list' command."""
    countries = api.get_all_countries()
    if not countries:
        print("Could not retrieve the list of countries.")
        return
    
    for country in countries:
        print(country)
