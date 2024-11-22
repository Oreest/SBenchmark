import statistics
from typing import List

from app.models.benchmark_model import BenchmarkResult


# Utility Function to Calculate Averages
def calculate_average(results: List[BenchmarkResult]):
    # for result in results['benchmarking_results']:
    #     print(result)
    return {
        "average_token_count": statistics.mean(result['token_count'] for result in results),
        "average_time_to_first_token": statistics.mean(result['time_to_first_token'] for result in results),
        "average_time_per_output_token": statistics.mean(result['time_per_output_token'] for result in results),
        "average_total_generation_time": statistics.mean(result['total_generation_time'] for result in results),
    }