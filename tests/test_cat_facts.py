from unittest.mock import *
from lib.cat_facts import *

"""
The purpose of cat facts is to return a random fact about cats
When we call provide function, it'll return
formatted sentence including a cat fact
"""

"""
Test to determine when we call provide, it uses an API to
generate a random cat fact, and returns it in a sentence
"""

def test_return_random_cat_fact():
    mock_requester = Mock()
    mock_response = Mock()
    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {"fact":"A female cat is called a queen or a molly."}
    cat_fact = CatFacts(mock_requester)
    assert cat_fact.provide() == "Cat fact: A female cat is called a queen or a molly."