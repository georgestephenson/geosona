import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import '@testing-library/jest-dom/vitest'
import App from './App'

// Mock react-map-gl to avoid MapLibre rendering issues in tests
vi.mock('react-map-gl/maplibre', () => ({
  default: ({ children }: { children?: React.ReactNode }) => <div data-testid="map">{children}</div>,
  NavigationControl: () => <div data-testid="nav-control" />,
  GeolocateControl: () => <div data-testid="geolocate-control" />,
  ScaleControl: () => <div data-testid="scale-control" />,
}))

describe('App', () => {
  it('renders the application header', () => {
    render(<App />)
    
    expect(screen.getByText('geosona')).toBeInTheDocument()
    expect(screen.getByText('global music artist graph')).toBeInTheDocument()
  })

  it('renders the tech stack info panel', () => {
    render(<App />)
    
    expect(screen.getByText('Tech Stack Demo')).toBeInTheDocument()
    expect(screen.getByText('✓ React 19 + TypeScript')).toBeInTheDocument()
    expect(screen.getByText('✓ MapLibre GL JS')).toBeInTheDocument()
    expect(screen.getByText('✓ Tailwind CSS')).toBeInTheDocument()
  })

  it('renders the map component', () => {
    render(<App />)
    
    expect(screen.getByTestId('map')).toBeInTheDocument()
  })

  it('renders map controls', () => {
    render(<App />)
    
    expect(screen.getByTestId('nav-control')).toBeInTheDocument()
    expect(screen.getByTestId('geolocate-control')).toBeInTheDocument()
    expect(screen.getByTestId('scale-control')).toBeInTheDocument()
  })
})
