import functools

from neo4j import GraphDatabase
from pydantic import BaseModel, Field

from cypher_ai_helper.main import cypher_query, execute_query
from cypher_ai_helper.utils import pydantic_models_to_str


def test_cypher_query_with_execution():
    """
    Test cypher_query with execution of the query

    :return:
    """

    class User(BaseModel):
        """
        A User class
        """
        id: int = Field(..., description="The id of the user")
        name: str = Field(..., description="The name of the user")
        email: str = Field(..., description="The email of the user")

    class Post(BaseModel):
        """
        A Post class
        """
        id: int = Field(..., description="The id of the post")
        title: str = Field(..., description="The title of the post")
        body: str = Field(..., description="The body of the post")
        user_name: str = Field(..., description="The name of the user who created the post")

    _q = cypher_query("del-all", pydantic_models_to_str([User, Post]),
                      "Delete all nodes and relations",
                      input_vars=[],
                      func=functools.partial(execute_query, driver=GraphDatabase.driver("bolt://localhost:27687",
                                                                                        auth=("neo4j",
                                                                                              "pleaseletmein")),
                                             database="neo4j"))

    # _q = cypher_query("new-user-constraint", pydantic_models_to_str([User, Post]),
    #                   "Add new constraint that User's name must be unique",
    #                   input_vars=[],
    #                   func=functools.partial(execute_query, driver=GraphDatabase.driver("bolt://localhost:27687",
    #                                                                                     auth=("neo4j",
    #                                                                                           "pleaseletmein")),
    #                                          database="neo4j", params={}))
    _q = cypher_query("new-user", pydantic_models_to_str([User, Post]),
                      "Create a new user and return the created user",
                      input_vars=["id", "name", "email"],
                      func=functools.partial(execute_query, driver=GraphDatabase.driver("bolt://localhost:27687",
                                                                                        auth=("neo4j",
                                                                                              "pleaseletmein")),
                                             database="neo4j", params={"id": 2, "name": "post_user", "email": "test"}))
    # _q = cypher_query("new-post", pydantic_models_to_str([User, Post]),
    #                   "Create a new post and link it to given user. Name the relation 'POSTED_BY'",
    #                   input_vars=["id", "title", "body", "user_name"],
    #                   func=functools.partial(execute_query, driver=GraphDatabase.driver("bolt://localhost:27687",
    #                                                                                     auth=("neo4j",
    #                                                                                           "pleaseletmein")),
    #                                          database="neo4j",
    #                                          params={"id": 3, "title": "My second post",
    #                                                  "body": "second post is better",
    #                                                  "user_name": "post_user"}))

    driver = GraphDatabase.driver("bolt://localhost:27687", auth=("neo4j", "pleaseletmein"))
    with driver.session(database='neo4j') as session:
        result = session.run("MATCH (n:User) RETURN n")
        assert result.single()['n']['name'] == 'post_user'
