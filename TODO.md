# TODO

## Testing

### Future: Add Playwright for E2E Testing
- Install: `pnpm add -D @playwright/test`
- Test map interactions, artist search, graph visualization
- Set up in CI/CD pipeline

## Deployment & Infrastructure

### Frontend Docker Setup
- Create multi-stage Dockerfile (build → nginx)
- Create nginx.conf for SPA routing and asset caching
- Add .dockerignore file
- Configure environment variables (.env for VITE_API_URL)
- Note: Use Docker for production builds only, run `pnpm dev` locally for development

### Docker Compose Orchestration
- Update infrastructure/docker-compose.yml with all services:
  - PostgreSQL + PostGIS
  - Neo4j
  - Backend (Python/FastAPI)
  - Frontend (Nginx serving static build)
- Set up service dependencies and networking
- Configure volume persistence for databases
