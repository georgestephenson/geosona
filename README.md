# geosona

global music artist graph

## Overview

An interactive world map visualization exploring music artists, their geographic origins, and the connections between them through collaborations and influences. This project aims to provide a more globally representative view of music history, addressing the Western bias present in many popular music lists and platforms.

## Motivation

Traditional music discovery platforms (Spotify, Apple Music) and "greatest of all time" lists tend to have significant Western bias. Large populations in China, India, Africa, and the Middle East have rich musical traditions that are underrepresented. 

Within Western canonical music, there is a clear lineage of influence between historical music and later artists and genres. However, there are other canons of music, and examples of where (and when) artists have been isolated from the international music scene. Moreover, at a local scale there have been many music scenes that seemingly exist in their own miniature bubble, within cities like Kingston, Seoul, or Seattle. Therefore, it's interesting to consider to what extent influences exist in bubbles, and to what extent they transcend geographic boundaries.

Geosona aims to visualize music as a truly global phenomenon, showing how artists from different regions influence each other and collaborate across borders.

## Tech Stack

### Frontend
- **React 19 + TypeScript** - Modern UI framework
- **Vite** - Fast build tool and dev server
- **MapLibre GL JS** - Open-source map rendering
- **Tailwind CSS v4** - Utility-first styling
- **TanStack Query** - Data fetching and caching
- **Vitest** - Unit testing

### Backend (Planned)
- **Python + FastAPI** - High-performance API server
- **Neo4j** - Graph database for artist relationships (influences, collaborations)
- **PostgreSQL + PostGIS** - Geospatial data for artist locations and map features

### Data Pipeline (Planned)
- **Python ETL scripts** - Data extraction and transformation

### Infrastructure
- **Docker + Docker Compose** - Containerization and orchestration

## Project Structure

```
geosona/
├── frontend/           # React + MapLibre application
├── backend/            # FastAPI server (planned)
├── data-pipeline/      # ETL scripts (planned)
├── database/           # DB schemas and migrations (planned)
├── infrastructure/     # Docker configs (planned)
├── docs/               # Documentation
└── TODO.md             # Project roadmap
```

## Getting Started

### Frontend Development

```bash
cd frontend
pnpm install
pnpm dev
```

See [frontend/README.md](frontend/README.md) for detailed setup instructions.

### Full Stack (Coming Soon)

```bash
cd infrastructure
docker-compose up
```

## License

See [LICENSE](LICENSE) file for details.