# Inflation & GDP Tracker CLI

A Python-based command-line tool to fetch, display, and compare economic information for countries, including GDP, inflation, population, and currency data.

---

## 🚀 Features

- **Country Data:** Get key economic indicators for any country.
- **Compare:** See a side-by-side comparison of two countries.
- **Currency Info:** Look up a country's official currency.
- **List All:** Get a list of all supported countries.

---

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gemini/econcli.git
    cd econcli
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install the CLI:**
    ```bash
    python setup.py install
    ```

---

## Usage

The CLI can be run using the `econ` command.

### Commands

**1. Get Country Information**

Displays GDP, inflation, population, currency, and region for a specific country.

```bash
$ econ country japan

🇯🇵 Japan
GDP (per capita): $42,000
Inflation rate: 2.3%
Population: 125,700,000
Currency: Japanese Yen (JPY)
Region: Asia
```

**2. Compare Two Countries**

Shows a side-by-side comparison of GDP and inflation rates.

```bash
$ econ compare germany france

Comparing Germany vs. France

| Metric         | Germany   | France    |
|----------------|-----------|-----------|
| GDP (per capita) | $52,000   | $45,000   |
| Inflation Rate | 3.1%      | 2.8%      |
```

**3. Get Currency Information**

Shows the country’s official currency name and code.

```bash
$ econ currency brazil

Brazilian Real (BRL)
```

**4. List All Supported Countries**

Provides a list of all countries available through the API.

```bash
$ econ list

Afghanistan
Albania
Algeria
...
```

---

##  APIs Used

This tool relies on the following free, no-authentication APIs:

-   **REST Countries API (`https://restcountries.com/v3.1/`):** Used for population, currency, region, and the general list of countries.
-   **World Bank API (`https://api.worldbank.org/v2/`):** Used to fetch GDP and inflation statistics.

Data is retrieved via simple HTTP GET requests. The tool handles cases where data may be missing or APIs are unavailable.
