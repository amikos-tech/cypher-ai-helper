from neo4j import GraphDatabase


def test_neo4j():
    driver = GraphDatabase.driver("bolt://localhost:27687", auth=("neo4j", "pleaseletmein"))
    with driver.session(database='neo4j') as session:
        result = session.run("MATCH (n) RETURN n")
        print(result.data())
