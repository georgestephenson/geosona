# Infrastructure

Docker Compose configuration for Geosona services.

## Quick Start

1. Set required environment variables:
   ```bash
   export POSTGRES_PASSWORD="your-secure-password"
   export NEO4J_PASSWORD="your-secure-password"
   ```

2. Start all services:
   ```bash
   docker compose up -d
   ```

3. Load Neo4j sample data:
   ```bash
   docker exec -it geosona-neo4j cypher-shell -u neo4j -p $NEO4J_PASSWORD -f /import/01-artist-influences.cypher
   ```

## Services

### PostgreSQL + PostGIS
- **Image**: `postgis/postgis:17-3.5`
- **Container**: `geosona-postgres`
- **Ports**: 5432
- **Volumes**: `postgres_data`, initialization scripts from `../database/postgres/init/`
- **Health check**: `pg_isready`

### Neo4j
- **Image**: `neo4j:5.26.19-community`
- **Container**: `geosona-neo4j`
- **Ports**: 7474 (HTTP), 7687 (Bolt)
- **Volumes**: `neo4j_data`, `neo4j_logs`, initialization scripts from `../database/neo4j/init/`
- **Plugins**: APOC
- **Health check**: `cypher-shell`

## Management Commands

### Start services
```bash
docker compose up -d
```

### Stop services
```bash
docker compose stop
```

### Stop and remove containers (keeps data)
```bash
docker compose down
```

### Stop and remove all data
```bash
docker compose down -v
```

### View logs
```bash
docker compose logs -f postgres
docker compose logs -f neo4j
```

### Check health status
```bash
docker ps
```

### Run health checks manually
```bash
docker exec geosona-postgres pg_isready -U geosona_user -d geosona
docker exec geosona-neo4j cypher-shell -u neo4j -p $NEO4J_PASSWORD 'RETURN 1'
```

## Environment Variables

Required environment variables:
- `POSTGRES_PASSWORD` - Password for PostgreSQL user
- `NEO4J_PASSWORD` - Password for Neo4j user

These must be set before running `docker compose up`.
