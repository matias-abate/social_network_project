# app/services/relationship_service.py

from app.database import neo4j_driver

class RelationshipService:

    @staticmethod
    def create_relationship(user_from: str, user_to: str, relationship_type: str):
        with neo4j_driver.session() as session:
            session.run(
                """
                MATCH (a:User {username: $user_from}), (b:User {username: $user_to})
                MERGE (a)-[r:RELATIONSHIP {type: $relationship_type}]->(b)
                RETURN a, b, r
                """,
                user_from=user_from,
                user_to=user_to,
                relationship_type=relationship_type
            )

    @staticmethod
    def get_relationships(username: str):
        relationships = []
        with neo4j_driver.session() as session:
            result = session.run(
                """
                MATCH (a:User {username: $username})-[r:RELATIONSHIP]->(b:User)
                RETURN b.username AS user_to, r.type AS relationship_type
                """,
                username=username
            )
            for record in result:
                relationships.append({
                    "user_from": username,
                    "user_to": record["user_to"],
                    "relationship_type": record["relationship_type"],
                })
        return relationships

    @staticmethod
    def delete_relationship(user_from: str, user_to: str):
        with neo4j_driver.session() as session:
            session.run(
                """
                MATCH (a:User {username: $user_from})-[r:RELATIONSHIP]->(b:User {username: $user_to})
                DELETE r
                """,
                user_from=user_from,
                user_to=user_to
            )
