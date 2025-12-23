import { useState } from 'react'
import Map, { NavigationControl, GeolocateControl, ScaleControl } from 'react-map-gl/maplibre'
import 'maplibre-gl/dist/maplibre-gl.css'

function App() {
  const [viewState, setViewState] = useState({
    longitude: 0,
    latitude: 20,
    zoom: 2
  })

  return (
    <div className="flex flex-col h-screen w-screen bg-gray-900">
      {/* Header */}
      <header className="bg-gray-800 text-white p-4 shadow-lg shrink-0">
        <div className="container mx-auto flex items-center justify-between">
          <h1 className="text-2xl font-bold">geosona</h1>
          <p className="text-gray-400 text-sm">global music artist graph</p>
        </div>
      </header>

      {/* Map Container */}
      <div className="flex-1 w-full relative">
        <div className="w-full h-full">
          <Map
            {...viewState}
            onMove={(evt) => setViewState(evt.viewState)}
            mapStyle="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
            style={{ width: '100%', height: '100%' }}
          >
            <NavigationControl position="top-right" />
            <GeolocateControl position="top-right" />
            <ScaleControl />
          </Map>
        </div>

        {/* Overlay Info */}
        <div className="absolute bottom-4 left-4 bg-white/90 backdrop-blur-sm rounded-lg shadow-lg p-4 max-w-sm">
          <h2 className="text-lg font-semibold text-gray-800 mb-2">Tech Stack Demo</h2>
          <ul className="text-sm text-gray-600 space-y-1">
            <li>✓ React 19 + TypeScript</li>
            <li>✓ MapLibre GL JS</li>
            <li>✓ react-map-gl</li>
            <li>✓ Tailwind CSS</li>
            <li>✓ Vite</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default App
