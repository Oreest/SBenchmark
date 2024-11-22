from datetime import datetime

from pydantic import BaseModel


class BenchmarkResult(BaseModel):
    request_id: str
    prompt_text: str
    generated_text: str
    token_count: int
    time_to_first_token: float
    time_per_output_token: float
    total_generation_time: float
    timestamp: datetime
