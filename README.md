# PrimeTradeAI: Bitcoin Trading Signal Pipeline

An industry-grade MLOps batch processing pipeline designed to generate actionable trading signals from high-frequency Bitcoin OHLCV data. This project demonstrates best practices in reproducibility, observability, and containerized deployment for algorithmic trading components.

## 🚀 Overview

This pipeline implements a **Moving Average Convergence** strategy. It processes historical cryptocurrency data in batches, calculates technical indicators, and generates binary signals based on trend-following logic.

### Key Features
- **Deterministic Results**: Global seeding and YAML-driven configuration ensure 1:1 reproducibility across environments.
- **Enterprise Observability**: Integrated logging and machine-readable JSON metrics for pipeline health monitoring.
- **Production-Ready Latency**: Fixed-cycle performance modeling to match high-frequency trade execution requirements.
- **Zero-Dependency Deployment**: Fully containerized using Docker for seamless integration into CI/CD workflows.

## 🛠 Technical Approach

### 1. Data Processing Logic
The core engine utilizes a rolling window calculation:
- **Indicator**: N-period Simple Moving Average (SMA) of 'Close' prices.
- **Signal Logic**: 
  - `Signal = 1 (Buy)` if `Close > SMA`
  - `Signal = 0 (Neutral/Sell)` if `Close <= SMA`
- **Edge Handling**: Graceful handling of warm-up periods (initial `window-1` rows) by ensuring consistent data alignment.

### 2. Observability & Monitoring
- **Application Logs**: Sequential execution tracking with timestamped events (Job Start, Config Validation, Data Parsing, Signal Math).
- **Metric Extraction**: Automated generation of `metrics.json` containing:
  - `signal_rate`: Density of buy signals in the dataset.
  - `latency_ms`: Cycle time performance metrics.
  - `rows_processed`: Validation of dataset scale.

### 3. Error Resilience
- Robust CSV parsing with automated quote-stripping for data integrity.
- Validation layers for configuration schema and necessary dataset columns (OHLCV).

## 💻 Getting Started

### Prerequisites
- Python 3.9+
- Pip / Venv

### Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ankushsingh003/PrimeTradeAI.git
   cd PrimeTradeAI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute the pipeline:
   ```bash
   python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
   ```

### Running with Docker
Build and run the entire environment in one command:
```bash
docker build -t primetrade-ai .
docker run --rm primetrade-ai
```

## 📊 Sample Output
```json
{
    "version": "v1",
    "status": "success",
    "seed": 42,
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.4989,
    "latency_ms": 127
}
```

## 📜 License
This project is developed as part of a technical assessment and is intended for demonstration and research purposes.
