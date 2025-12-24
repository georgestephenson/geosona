# Neo4j Database

This directory contains initialization scripts for the Neo4j graph database.

## Access

- **Browser UI**: http://localhost:7474
- **Bolt Protocol**: bolt://localhost:7687
- **Username**: `neo4j`
- **Password**: Set via `NEO4J_PASSWORD` environment variable

## Connect to Database

**Via Browser:**
Open http://localhost:7474 and login with the credentials above.

**Via cypher-shell:**
```bash
docker exec -it geosona-neo4j cypher-shell -u neo4j -p $NEO4J_PASSWORD
```

## Initialization

The Cypher scripts in the `init/` directory are available in the container at `/import`. To execute them after starting the container:

```bash
docker exec -it geosona-neo4j cypher-shell -u neo4j -p $NEO4J_PASSWORD -f /import/01-artist-influences.cypher
```

## Example Queries

### Find all artists influenced by The Beatles
```cypher
MATCH (beatles:Artist {name: 'The Beatles'})-[:INFLUENCED]->(influenced)
RETURN influenced.name, influenced.genre
```

### Find influence chains (who influenced who)
```cypher
MATCH path = (a:Artist)-[:INFLUENCED*1..3]->(b:Artist)
RETURN a.name AS influencer, b.name AS influenced, length(path) AS degrees
ORDER BY degrees, a.name
```

### Find common influencers between two artists
```cypher
MATCH (influencer:Artist)-[:INFLUENCED]->(a:Artist {name: 'The Beatles'})
MATCH (influencer)-[:INFLUENCED]->(b:Artist {name: 'The Rolling Stones'})
RETURN influencer.name, influencer.genre
```

### Find the most influential artists
```cypher
MATCH (a:Artist)-[i:INFLUENCED]->()
RETURN a.name, a.genre, count(i) AS influence_count
ORDER BY influence_count DESC
```
