import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from app.Database.database import load_database
from app.Utility.average import calculate_average

load_dotenv()

# Environment variable to determine DEBUG mode
DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() == "true"
if DEBUG:
    try:
        benchmark_results = load_database(DEBUG)
    except RuntimeError as e:
        # Handle database load issues (e.g., DEBUG disabled, missing file)
        benchmark_results = []
        print(str(e))

print(benchmark_results)

# Initialize FastAPI app
app = FastAPI(title="SuperBenchmark", description="A FastAPI app for benchmarking tasks", version="0.1")


@app.get("/")
async def read_root():
    return {"message": "Welcome to SuperBenchmark!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# HTTP GET /results/average
@app.get("/results/average")
async def get_average_results():
    if not benchmark_results:
        raise HTTPException(status_code=404, detail="No benchmarking results found.")
    return calculate_average(benchmark_results)


# HTTP GET /results/average/{start_time}/{end_time}
@app.get("/results/average/{start_time}/{end_time}")
async def get_average_results_within_window(start_time: str, end_time: str):
    from datetime import datetime

    try:
        start_time_dt = datetime.fromisoformat(start_time)
        end_time_dt = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid timestamp format. Use ISO format (YYYY-MM-DDTHH:MM:SS).")

    # Filter results within the time window
    filtered_results = [
        result for result in benchmark_results
        if start_time_dt <= datetime.fromisoformat(result["timestamp"]) <= end_time_dt
    ]

    if not filtered_results:
        raise HTTPException(status_code=404, detail="No benchmarking results found within the specified time window.")

    return calculate_average(filtered_results)
