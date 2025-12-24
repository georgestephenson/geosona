-- PostgreSQL + PostGIS initialization script
-- This script runs automatically when the database is first created

-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Verify installation
SELECT PostGIS_version();

-- Example: Create a table for artist locations
CREATE TABLE IF NOT EXISTS artist_locations (
    id SERIAL PRIMARY KEY,
    artist_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    location GEOGRAPHY(POINT, 4326),
    city VARCHAR(255),
    country VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create spatial index for efficient geographic queries
CREATE INDEX idx_artist_locations_geog ON artist_locations USING GIST(location);
