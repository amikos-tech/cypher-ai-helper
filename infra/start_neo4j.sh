#!/usr/bin/env bash

echo "Starting Neo4j"

docker run \
    --name neo4j \
    -p 27474:7474 -p 27687:7687 \
    -d \
    -e NEO4J_AUTH=neo4j/pleaseletmein \
    -e NEO4J_PLUGINS=\[\"apoc\"\]  \
    neo4j:latest