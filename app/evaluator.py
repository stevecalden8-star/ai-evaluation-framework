import asyncio
from app.utils import validate_input

async def evaluate_task(data: dict) -> str:
    validate_input(data)
    await asyncio.sleep(0.1)
    return f"Processed task: {data['task']}"