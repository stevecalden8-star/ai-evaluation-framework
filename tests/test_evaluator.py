import pytest
from app.evaluator import evaluate_task

@pytest.mark.asyncio
async def test_evaluate_task(sample_data):
    result = await evaluate_task(sample_data)
    assert "Processed task" in result