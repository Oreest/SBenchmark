from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="SuperBenchmark", description="A FastAPI app for benchmarking tasks", version="0.1")


@app.get("/")
async def read_root():
    return {"message": "Welcome to SuperBenchmark!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/benchmark")
async def run_benchmark(data: dict):
    # Dummy benchmarking logic
    result = {"task": data.get("task", "default_task"), "status": "completed"}
    return result
