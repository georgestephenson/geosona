# PostgreSQL Database

This directory contains initialization scripts for the PostgreSQL + PostGIS database.

## Access

- **Host**: localhost
- **Port**: 5432
- **Database**: `geosona`
- **Username**: `geosona_user`
- **Password**: Set via `POSTGRES_PASSWORD` environment variable

## Connect to Database

```bash
docker exec -it geosona-postgres psql -U geosona_user -d geosona
```

## Initialization

SQL scripts in the `init/` directory are automatically executed when the database is first created, in alphabetical order.

## Verify PostGIS

```bash
docker exec -it geosona-postgres psql -U geosona_user -d geosona -c "SELECT PostGIS_version();"
```

## Common Queries

### List all tables
```sql
\dt
```

### List PostGIS functions
```sql
SELECT proname FROM pg_proc WHERE proname LIKE 'st_%' LIMIT 10;
```

### Check spatial reference systems
```sql
SELECT srid, auth_name, srtext FROM spatial_ref_sys LIMIT 5;
```
