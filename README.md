# Assessment Service

Student assessment handling service for the Tutor Stack.

## Features

- Answer grading
- Score calculation
- RESTful API with FastAPI

## Development

### Prerequisites

- Python 3.11+
- Docker (optional)

### Local Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # for development
   ```

3. Run the service:
   ```bash
   uvicorn app.main:app --reload
   ```

### Using Docker

```bash
docker build -t assessment-service .
docker run -p 8000:8000 assessment-service
```

### Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=term-missing
```

### Code Quality

```bash
# Format code
black app/ tests/
isort app/ tests/

# Run linters
flake8 app/ tests/
mypy app/ tests/
```

## Branch Protection Rules

This repository follows these branch protection rules:
1. `main` branch is protected
2. Pull requests require:
   - 1 reviewer approval
   - Passing CI checks
   - Up-to-date branch
3. Force pushes are disabled
4. Branch is required to be up to date before merging

## Deployment

The service can be deployed to:
- Google Cloud Run (recommended)
- Any Kubernetes cluster
- Any platform supporting Docker containers

See [Deployment Guide](DEPLOYMENT.md) for detailed instructions.

## API Documentation

When running, visit:
- OpenAPI UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

None required for basic operation.

## CI/CD

GitHub Actions workflows handle:
- Running tests
- Code quality checks
- Building Docker image
- (Optional) Deployment to chosen platform # CI Test
