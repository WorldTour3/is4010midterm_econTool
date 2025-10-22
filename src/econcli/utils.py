"""Utility functions for formatting data."""

def format_population(population):
    """Formats a population number with commas."""
    if population is None:
        return "N/A"
    return f"{population:,}"

def format_currency(value, symbol="$"):
    """Formats a currency value."""
    if value is None:
        return "N/A"
    return f"{symbol}{value:,.0f}"

def format_percentage(value):
    """Formats a value as a percentage."""
    if value is None:
        return "N/A"
    return f"{value:.1f}%"
