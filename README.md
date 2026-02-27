# MLOps Bitcoin Trading Signal Pipeline

A minimal MLOps-style batch job that generates trading signals from OHLCV Bitcoin data based on a rolling mean comparison.

## Logic
- The program computes a rolling mean of the `close` price using a configurable `window`.
- A signal is generated for each row:
  - `signal = 1` if `close > rolling_mean`
  - `signal = 0` otherwise
- Reproducibility is ensured via a fixed `seed` for any random operations.

## Requirements
- Python 3.9+
- pandas
- numpy
- PyYAML

## Local Setup & Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```bash
   python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
   ```

## Docker Execution

1. Build the image:
   ```bash
   docker build -t mlops-task .
   ```

2. Run the container:
   ```bash
   docker run --rm mlops-task
   ```

The container includes `data.csv` and `config.yaml`, produces `metrics.json` and `run.log`, and prints the final metrics JSON to stdout.

## Example Metrics
```json
{
    "version": "v1",
    "status": "success",
    "seed": 42,
    "rows_processed": 10000,
    "metric": "signal_rate",
    "value": 0.499,
    "latency_ms": 34
}
```
