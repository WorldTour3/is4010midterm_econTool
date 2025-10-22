# Project Structure and Flow

This document explains the internal structure of the **Inflation & GDP Tracker CLI** and how its components interact.

---

## 📂 Module Overview

The project is organized into a modular structure to separate concerns and improve maintainability.

```
econcli/
├── econcli/            # Main package
│   ├── __init__.py     # Makes the directory a Python package
│   ├── main.py         # CLI entry point, handles argument parsing
│   ├── api.py          # All external API call logic
│   ├── commands.py     # Implements the logic for each CLI command
│   └── utils.py        # Helper functions for formatting and display
├── tests/              # Test suite
│   ├── test_api.py     # Tests for the api.py module
│   └── test_commands.py# Tests for the commands.py module
├── README.md           # User-facing documentation
├── AGENTS.md           # This file: developer-facing documentation
├── requirements.txt    # Project dependencies
└── setup.py            # Package setup and installation script
```

### Module Responsibilities

-   **`main.py`**: The user's entry point. It uses Python's `argparse` library to define the CLI commands (`country`, `compare`, etc.) and their expected arguments. It is responsible for parsing the user's input and calling the correct function in `commands.py`.

-   **`commands.py`**: Contains the core application logic. Each function in this module corresponds to a CLI command. It orchestrates calls to `api.py` to fetch data and uses `utils.py` to format it before printing the output to the console.

-   **`api.py`**: Acts as a data layer. It is solely responsible for communicating with the external REST Countries and World Bank APIs. It abstracts away the complexity of making HTTP requests and parsing JSON responses. It also includes error handling for network issues or missing data.

-   **`utils.py`**: A collection of stateless helper functions that are used across the application. This includes functions for formatting numbers (like population and currency) and creating styled output (like tables).

-   **`tests/`**: Contains all unit tests. The tests use `pytest` and `pytest-mock` to simulate API responses, allowing for reliable and fast testing without making actual network requests.

---

## ⚙️ Execution Flow

Here is the typical flow when a user runs a command:

1.  **User Input**: The user executes a command in their terminal (e.g., `econ country canada`).

2.  **Entry Point**: The `main` function in `main.py` is triggered via the `console_scripts` entry point defined in `setup.py`.

3.  **Argument Parsing**: `argparse` parses the command-line arguments (`country` and `canada`). Based on the command, `main.py` determines that the `handle_country_command` function in `commands.py` should be called.

4.  **Command Logic**: `commands.py` executes the handler. The handler calls the relevant functions in `api.py` to fetch the required data (e.g., `get_country_info('canada')`, `get_gdp('CAN')`).

5.  **API Calls**: `api.py` constructs the appropriate API request URLs and uses the `requests` library to make HTTP GET calls. It parses the JSON responses and returns structured data (or `None` if data is not found).

6.  **Data Formatting**: The command handler in `commands.py` receives the data from the API module. It then uses functions from `utils.py` to format the population numbers, currency values, and construct the final output string.

7.  **Output**: The formatted string is printed to the console for the user to see.

This decoupled architecture ensures that each part of the application has a single responsibility, making it easier to test, debug, and extend in the future.
