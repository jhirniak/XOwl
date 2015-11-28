## Neo4j database setup

1. Download English Wikipedia dump [enwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2).

2. Clone [graphipedia](https://github.com/mirkonasato/graphipedia) and build the package using `mvn package` from the project directory.

3. Convert the Wikipedia dump to pages and links `XML` representation:

```bash
lbzip2 -dc enwiki-latest-pages-articles.xml.bz2 | java -classpath $GRAPHP/graphipedia-dataimport.jar org.graphipedia.dataimport.ExtractLinks - enwiki-links.xml
```

4. Convert `XML` Wikipedia graph to `Neo4j` GraphDB:

```bash
java -Xmx3G -classpath $GRAPHP/graphipedia-dataimport.jar org.graphipedia.dataimport.neo4j.ImportGraph enwiki-links.xml wiki-small.db
```

5. Query for Bacon distance (Milgram experiment):

```cypher
MATCH p=shortestPath(
  (p1:Page)-[*]-(p2:Page)
)
RETURN DISTINCT p1.title, p2.title, sum(length(p))/count(p)
```

Here we use `shortestPath` which uses Floyd-Warshall algorithm, `[*]` to mean any pages `p1` and `p2` that are connected, but we also use `DISTINCT` to mean that we want to find only one shortest path between `p1` and `p2` as there may be multiple.