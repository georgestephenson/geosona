# Infrastructure

Docker configuration for Geosona services.

## Quick Start

1. Copy the environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set a secure password for `POSTGRES_PASSWORD`

3. Start the database:
   ```bash
   docker-compose up -d
   ```

4. Verify PostGIS is installed:
   ```bash
   docker exec -it geosona-postgres psql -U geosona_user -d geosona -c "SELECT PostGIS_version();"
   ```

## Services

### PostgreSQL + PostGIS
- **Image**: `postgis/postgis:17-3.5`
- **Port**: 5432
- **Database**: geosona
- **User**: geosona_user
- **Password**: Set in `.env` file

## Database Management

### Connect to database
```bash
docker exec -it geosona-postgres psql -U geosona_user -d geosona
```

### Stop services
```bash
docker-compose down
```

### Stop and remove data
```bash
docker-compose down -v
```

### View logs
```bash
docker-compose logs -f postgres
```

## Initialization Scripts

SQL scripts in `../database/postgres/init/` are automatically executed when the database is first created, in alphabetical order.
