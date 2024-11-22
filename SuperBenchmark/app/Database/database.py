import json
from datetime import datetime


def load_database(DEBUG):
    """
       Load the dummy database from a JSON file if DEBUG mode is enabled.
       Returns:
           List[dict]: A list of benchmarking results.
       Raises:
           RuntimeError: If DEBUG mode is not enabled or the file is missing.
       """
    if DEBUG:
        try:
            database_path = "app/Database/test_database.json"
            with open(database_path, "r") as f:
                benchmark_results = json.load(f)

                # Convert timestamps to datetime
                for result in benchmark_results:
                    if "timestamp" in result:
                        result["timestamp"] = datetime.fromisoformat(result["timestamp"])
                return benchmark_results['benchmarking_results']
        except FileNotFoundError:
            raise RuntimeError(f"DEBUG mode is enabled, but '{database_path}' file not found.")
        except json.JSONDecodeError:
            raise RuntimeError(f"Failed to parse '{database_path}'. Ensure it's a valid JSON file.")
    else:
        raise RuntimeError(
            "The feature is not ready for live use yet. Set SUPERBENCHMARK_DEBUG to 'true' to enable DEBUG mode.")