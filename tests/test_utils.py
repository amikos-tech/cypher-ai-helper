import dataclasses
from unittest import TestCase

from pydantic import BaseModel, Field

from cypher_ai_helper.utils import class_definition_in_str_for_dataclasses, pydantic_model_to_str, \
    pydantic_models_to_str


def test_class_definition_in_str_for_dataclasses():
    """
    This function tests the class_definition_in_str_for_dataclasses function

    :return:
    """

    @dataclasses.dataclass
    class User:
        """
        This is the User class.
        It has three fields: id, name, and email.
        """
        id: int
        name: str
        email: str

    assert "@dataclasses.dataclass" in class_definition_in_str_for_dataclasses(User)
    assert "class User:" in class_definition_in_str_for_dataclasses(User)
    assert "id: int" in class_definition_in_str_for_dataclasses(User)
    assert "name: str" in class_definition_in_str_for_dataclasses(User)
    assert "email: str" in class_definition_in_str_for_dataclasses(User)


def test_pydantic_model_to_str():
    """
    This function tests the pydantic_model_to_str function

    :return:
    """

    class User(BaseModel):
        """
        A User class
        """
        id: int = Field(..., description="The id of the user")
        name: str = Field(..., description="The name of the user")
        email: str = Field(..., description="The email of the user")

    assert "class User(BaseModel):" in pydantic_model_to_str(User)
    assert "id: int = Field(..., description=\"The id of the user\")" in pydantic_model_to_str(User)
    assert "name: str = Field(..., description=\"The name of the user\")" in pydantic_model_to_str(User)
    assert "email: str = Field(..., description=\"The email of the user\")" in pydantic_model_to_str(User)


def test_pydantic_models_to_str():
    """
    This function tests the pydantic_models_to_str function

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

    assert "class User(BaseModel):" in pydantic_models_to_str([User, Post])
    assert "id: int = Field(..., description=\"The id of the user\")" in pydantic_models_to_str([User, Post])
    assert "name: str = Field(..., description=\"The name of the user\")" in pydantic_models_to_str([User, Post])
    assert "email: str = Field(..., description=\"The email of the user\")" in pydantic_models_to_str([User, Post])
    assert "class Post(BaseModel):" in pydantic_models_to_str([User, Post])
    assert "id: int = Field(..., description=\"The id of the post\")" in pydantic_models_to_str([User, Post])
    assert "title: str = Field(..., description=\"The title of the post\")" in pydantic_models_to_str([User, Post])
    assert "body: str = Field(..., description=\"The body of the post\")" in pydantic_models_to_str([User, Post])
