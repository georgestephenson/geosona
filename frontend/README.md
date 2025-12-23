# Geosona Frontend

Interactive world map visualization for exploring music artists, their geographic origins, and connections through collaborations and influences.

## Tech Stack

- **React 19** - UI framework with TypeScript
- **Vite** - Fast build tool and dev server
- **MapLibre GL JS** - Open-source map rendering engine
- **react-map-gl** - React wrapper for MapLibre
- **Tailwind CSS v4** - Utility-first CSS framework
- **TanStack Query** - Data fetching and state management
- **Vitest** - Unit testing framework
- **React Testing Library** - Component testing utilities

## Getting Started

### Prerequisites

- Node.js 20+
- pnpm (or npm/yarn)

### Installation

```bash
pnpm install
```

### Development

```bash
pnpm dev
```

Open [http://localhost:5173](http://localhost:5173) to view the app.

### Testing

```bash
pnpm test              # Run tests in watch mode
pnpm test:ui          # Run tests with UI (requires @vitest/ui)
pnpm test:coverage    # Run with coverage report
```

### Build

```bash
pnpm build            # TypeScript compile + Vite build
pnpm preview          # Preview production build locally
```

### Linting

```bash
pnpm lint
```

## Current Features

- ✅ Interactive world map with dark theme
- ✅ Map controls (navigation, geolocation, scale)
- ✅ Responsive layout with Tailwind CSS
- ✅ TypeScript type safety
- ✅ Unit testing setup with Vitest
- ✅ Type-aware ESLint configuration

## Configuration

### ESLint

Type-aware linting is enabled with `recommendedTypeChecked` rules. Configuration in `eslint.config.js`.
