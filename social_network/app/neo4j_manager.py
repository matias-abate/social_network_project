from neo4j import GraphDatabase
import os

neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
neo4j_user = os.getenv("NEO4J_USER", "neo4j")
neo4j_pass = os.getenv("NEO4J_PASSWORD", "neo4j")

driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_pass))

def create_user_node(username):
    with driver.session() as session:
        session.run("CREATE (u:User {username: $username})", username=username)

def create_relationship(from_user, to_user, rel_type="FOLLOWS"):
    with driver.session() as session:
        session.run("""
            MATCH (a:User {username: $from_user}), (b:User {username: $to_user})
            MERGE (a)-[:{rel_type}]->(b)
        """.replace("{rel_type}", rel_type), from_user=from_user, to_user=to_user)