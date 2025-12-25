# TODO

## Documentation 

- Add ARCHITECTURE.md

## Testing

### Future: Add Playwright for E2E Testing
- Install: `pnpm add -D @playwright/test`
- Test map interactions, artist search, graph visualization
- Set up in CI/CD pipeline

## Deployment & Infrastructure

### Docker Compose Orchestration
- Update infrastructure/docker-compose.yml with all services:
  - Frontend (Nginx serving static build)
- Set up service dependencies and networking
- Configure volume persistence for databases
