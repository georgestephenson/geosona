// Create constraints and indexes for Artist nodes
CREATE CONSTRAINT artist_name IF NOT EXISTS FOR (a:Artist) REQUIRE a.name IS UNIQUE;
CREATE INDEX artist_genre IF NOT EXISTS FOR (a:Artist) ON (a.genre);

// Create Artist nodes
CREATE (beatles:Artist {
  name: 'The Beatles',
  genre: 'Rock',
  formed: 1960,
  country: 'United Kingdom'
});

CREATE (stones:Artist {
  name: 'The Rolling Stones',
  genre: 'Rock',
  formed: 1962,
  country: 'United Kingdom'
});

CREATE (dylan:Artist {
  name: 'Bob Dylan',
  genre: 'Folk/Rock',
  formed: 1959,
  country: 'United States'
});

CREATE (elvis:Artist {
  name: 'Elvis Presley',
  genre: 'Rock and Roll',
  formed: 1954,
  country: 'United States'
});

CREATE (chuck:Artist {
  name: 'Chuck Berry',
  genre: 'Rock and Roll',
  formed: 1955,
  country: 'United States'
});

CREATE (muddy:Artist {
  name: 'Muddy Waters',
  genre: 'Blues',
  formed: 1943,
  country: 'United States'
});

CREATE (little:Artist {
  name: 'Little Richard',
  genre: 'Rock and Roll',
  formed: 1951,
  country: 'United States'
});

CREATE (radiohead:Artist {
  name: 'Radiohead',
  genre: 'Alternative Rock',
  formed: 1985,
  country: 'United Kingdom'
});

CREATE (nirvana:Artist {
  name: 'Nirvana',
  genre: 'Grunge',
  formed: 1987,
  country: 'United States'
});

CREATE (pixies:Artist {
  name: 'Pixies',
  genre: 'Alternative Rock',
  formed: 1986,
  country: 'United States'
});

// Create INFLUENCED relationships with context
MATCH (chuck:Artist {name: 'Chuck Berry'})
MATCH (beatles:Artist {name: 'The Beatles'})
CREATE (chuck)-[:INFLUENCED {aspect: 'guitar style, songwriting', strength: 'major'}]->(beatles);

MATCH (chuck:Artist {name: 'Chuck Berry'})
MATCH (stones:Artist {name: 'The Rolling Stones'})
CREATE (chuck)-[:INFLUENCED {aspect: 'guitar riffs, stage presence', strength: 'major'}]->(stones);

MATCH (muddy:Artist {name: 'Muddy Waters'})
MATCH (stones:Artist {name: 'The Rolling Stones'})
CREATE (muddy)-[:INFLUENCED {aspect: 'blues foundation, sound', strength: 'major'}]->(stones);

MATCH (little:Artist {name: 'Little Richard'})
MATCH (beatles:Artist {name: 'The Beatles'})
CREATE (little)-[:INFLUENCED {aspect: 'vocal style, energy', strength: 'major'}]->(beatles);

MATCH (elvis:Artist {name: 'Elvis Presley'})
MATCH (beatles:Artist {name: 'The Beatles'})
CREATE (elvis)-[:INFLUENCED {aspect: 'performance style', strength: 'moderate'}]->(beatles);

MATCH (dylan:Artist {name: 'Bob Dylan'})
MATCH (beatles:Artist {name: 'The Beatles'})
CREATE (dylan)-[:INFLUENCED {aspect: 'lyrical depth, experimentation', strength: 'major'}]->(beatles);

MATCH (beatles:Artist {name: 'The Beatles'})
MATCH (radiohead:Artist {name: 'Radiohead'})
CREATE (beatles)-[:INFLUENCED {aspect: 'experimentation, studio innovation', strength: 'major'}]->(radiohead);

MATCH (pixies:Artist {name: 'Pixies'})
MATCH (nirvana:Artist {name: 'Nirvana'})
CREATE (pixies)-[:INFLUENCED {aspect: 'quiet-loud dynamics, song structure', strength: 'major'}]->(nirvana);

MATCH (nirvana:Artist {name: 'Nirvana'})
MATCH (radiohead:Artist {name: 'Radiohead'})
CREATE (nirvana)-[:INFLUENCED {aspect: 'raw emotion, authenticity', strength: 'moderate'}]->(radiohead);

MATCH (beatles:Artist {name: 'The Beatles'})
MATCH (nirvana:Artist {name: 'Nirvana'})
CREATE (beatles)-[:INFLUENCED {aspect: 'songwriting, melody', strength: 'moderate'}]->(nirvana);
