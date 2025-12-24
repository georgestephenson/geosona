# Geosona Backend

FastAPI-based REST API for the Geosona music artist geography and influence network application.

## Tech Stack

- Python 3.12 (LTS)
- FastAPI 0.115.6
- Uvicorn (ASGI server)

## Local Development

### Using Docker (Recommended)
```bash
# From the infrastructure directory
docker-compose up backend
```

The API will be available at `http://localhost:8000`


### Without Docker
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


# Run development server
uvicorn main:app --reload
```

**Note:** The virtual environment is needed for VS Code IntelliSense and linting, even if you're running the app in Docker. After creating the venv and installing dependencies, VS Code will automatically detect it.

## Testing

The project uses **pytest** for testing with coverage reporting.

### Running Tests Locally (Quick)
```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_main.py

# Run tests matching a pattern
pytest -k "test_health"

# Run with coverage report
pytest --cov=. --cov-report=term-missing

# View HTML coverage report
pytest --cov=. --cov-report=html
# Then open htmlcov/index.html in a browser
```

### Running Tests in Docker (Recommended for CI/validation)
```bash
# Run tests in the same environment as production
docker compose run --rm backend pytest

# Run with coverage
docker compose run --rm backend pytest --cov=. --cov-report=term-missing
```

### Version Consistency
⚠️ **Important:** The local venv is for IDE support only. Always run tests in Docker before committing to ensure consistency with the production environment.

- `requirements.txt` - High-level dependencies (what you want)
- `requirements.lock` - Exact versions (pinned via `pip freeze`)
- Local venv uses same `requirements.txt` as Docker for consistency
- Run `pip freeze > requirements.lock` after updating dependencies

### Test Structure
- `tests/conftest.py` - Shared fixtures and test configuration
- `tests/test_main.py` - Tests for main API endpoints

