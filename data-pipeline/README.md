# Geosona Data Pipeline

ETL pipeline for extracting music artist data from various sources, transforming it, and loading into Neo4j and PostgreSQL.

## Architecture

```
Extract → Transform → Load
   ↓          ↓         ↓
  APIs    Cleaning   Databases
```

**Extract:** Pull data from MusicBrainz, Wikidata, etc.
**Transform:** Clean, deduplicate, geocode locations
**Load:** Write to Neo4j (relationships) and PostgreSQL (geospatial data)

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL with PostGIS (running locally or via Docker)
- Neo4j (running locally or via Docker)

### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment template
cp .env.example .env
# Edit .env with your database credentials
```