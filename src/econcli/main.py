"""Main entry point for the CLI."""

import argparse
from . import commands

def main():
    """Parses arguments and calls the appropriate command handler."""
    parser = argparse.ArgumentParser(description="A CLI tool for economic data.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Country command
    country_parser = subparsers.add_parser("country", help="Get data for a single country")
    country_parser.add_argument("name", type=str, help="The name or code of the country")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare two countries")
    compare_parser.add_argument("country1", type=str, help="The first country")
    compare_parser.add_argument("country2", type=str, help="The second country")

    # Currency command
    currency_parser = subparsers.add_parser("currency", help="Get currency info for a country")
    currency_parser.add_argument("country", type=str, help="The name of the country")

    # List command
    subparsers.add_parser("list", help="List all supported countries")

    args = parser.parse_args()

    if args.command == "country":
        commands.handle_country_command(args.name)
    elif args.command == "compare":
        commands.handle_compare_command(args.country1, args.country2)
    elif args.command == "currency":
        commands.handle_currency_command(args.country)
    elif args.command == "list":
        commands.handle_list_command()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
