# Geosona Architecture

## System Overview

Geosona is a full-stack application for visualizing global music artist geography, influences, and collaborations on an interactive map.

## Architecture Diagram

```mermaid
graph TB
    subgraph "Client Layer"
        UI[React Frontend<br/>MapLibre GL JS<br/>TanStack Query<br/>Tailwind CSS]
    end

    subgraph "API Layer"
        API[FastAPI Backend<br/>REST API<br/>CORS Enabled]
    end

    subgraph "Data Pipeline Layer"
        ETL[Python ETL Pipeline]
        MB[MusicBrainz API<br/>Extractor]
        WD[Wikidata API<br/>Extractor]
        Transform[Data Transformation<br/>Cleaning & Geocoding]
    end

    subgraph "Data Layer"
        NEO[(Neo4j Graph DB<br/>Artist Relationships<br/>Influences & Collaborations)]
        PG[(PostgreSQL + PostGIS<br/>Geospatial Data<br/>Artist Locations)]
    end

    subgraph "External Data Sources"
        MusicBrainz[MusicBrainz API]
        Wikidata[Wikidata API]
    end

    subgraph "Infrastructure"
        Docker[Docker Compose<br/>Container Orchestration]
    end

    UI -->|HTTP Requests| API
    API -->|Cypher Queries| NEO
    API -->|SQL/PostGIS Queries| PG
    
    MB -->|Extract Artist Data| MusicBrainz
    WD -->|Extract Metadata| Wikidata
    MB --> Transform
    WD --> Transform
    Transform -->|Load Relationships| NEO
    Transform -->|Load Geospatial Data| PG
    
    ETL -.-> MB
    ETL -.-> WD
    ETL -.-> Transform

    Docker -.->|Orchestrates| UI
    Docker -.->|Orchestrates| API
    Docker -.->|Orchestrates| NEO
    Docker -.->|Orchestrates| PG

    style UI fill:#61dafb,stroke:#333,stroke-width:2px,color:#000
    style API fill:#009688,stroke:#333,stroke-width:2px,color:#fff
    style NEO fill:#008cc1,stroke:#333,stroke-width:2px,color:#fff
    style PG fill:#336791,stroke:#333,stroke-width:2px,color:#fff
    style ETL fill:#ffd43b,stroke:#333,stroke-width:2px,color:#000
    style Transform fill:#ffd43b,stroke:#333,stroke-width:2px,color:#000
```
