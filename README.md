![CI](https://github.com/stevecalden8-star/ai-evaluation-framework/actions/workflows/python-tests.yml/badge.svg)
# AI Evaluation Framework

Production-grade AI task evaluation framework demonstrating:

- Async task execution
- Subprocess handling
- Input validation
- Functional and integration testing
- pytest fixtures
- Dockerized test execution
- CI-ready project structure

---

## Project Structure

ai-evaluation-framework/
│
├── app/
│   ├── evaluator.py
│   ├── runner.py
│   └── utils.py
│
├── tests/
│   ├── conftest.py
│   ├── test_evaluator.py
│   └── test_runner.py
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md

---

## How to Run Locally

### Install dependencies

pip install -r requirements.txt

### Run tests

pytest -v

---

## Run with Docker

docker build -t ai-eval .
docker run ai-eval

---

## Purpose


Designed to simulate AI model evaluation workflows with realistic edge-case testing and structured validation.


