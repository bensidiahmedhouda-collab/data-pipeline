# AMZN Stock Data Pipeline

An end-to-end data pipeline that fetches, transforms, and visualizes Amazon (AMZN) daily stock data using the Alpha Vantage API, with a live Streamlit dashboard deployed on Streamlit Cloud.

**Owner: Houda Ben Sidi Ahmed**

---

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for stock market data:

- **Extract** — fetches daily AMZN stock data from the Alpha Vantage API
- **Transform** — computes daily returns, 7-day moving average, and day direction (up/down)
- **Load** — saves the processed data to a local CSV file
- **Dashboard** — visualizes the data in an interactive Streamlit app

---

## Project Structure

```
data-pipeline/
├── src/
│   ├── extract.py       # Fetches data from Alpha Vantage API
│   ├── transform.py     # Computes derived metrics
│   └── load.py          # Saves data to CSV
├── dashboard.py         # Streamlit dashboard
├── main.py              # Runs the full ETL pipeline
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version for Streamlit Cloud
└── .github/
    └── workflows/
        └── pipeline.yml # CI/CD pipeline (GitHub Actions)
```

---

## Dashboard

The Streamlit dashboard displays:

- **This Week's Performance** — daily closing price and return (%) for the last 5 trading days, with green/red indicators
- **Closing Price Over Time** — line chart of historical closing prices
- **7-Day Moving Average** — smoothed price trend
- **Last 10 Rows** — raw data table

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/bensidiahmedhouda-collab/data-pipeline.git
cd data-pipeline
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file at the root of the project:

```
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

Get a free API key at [alphavantage.co](https://www.alphavantage.co/support/#api-key).

### 4. Run the pipeline

```bash
python main.py
```

### 5. Run the dashboard locally

```bash
streamlit run dashboard.py
```

---

## Deployment

The dashboard is deployed on **Streamlit Cloud**.

To configure the API key on Streamlit Cloud, go to your app settings → **Secrets** and add:

```toml
ALPHA_VANTAGE_API_KEY = "your_api_key_here"
```

---

## CI/CD

A GitHub Actions workflow runs the ETL pipeline automatically on every push to `main`, and is scheduled to run every weekday at 9:00 AM UTC.
