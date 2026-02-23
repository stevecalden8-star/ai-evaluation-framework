import logging

logging.basicConfig(level=logging.INFO)

def validate_input(data: dict) -> bool:
    if "task" not in data:
        raise ValueError("Missing 'task' key")
    return True