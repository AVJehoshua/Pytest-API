# File: tests/test_activity_suggester.py
from unittest.mock import *
from lib.activity_suggester import *
"""
When we call suggest, 
it returns a nice activity for us to do:
"""
def test_suggest_nice_activity_to_do():
    mock_requester = Mock()                     
    mock_response = Mock()  
    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {"activity":"Learn how to make an Alexa skill"}
    suggester = ActivitySuggester(mock_requester)
    assert suggester.suggest() == "Why not: Learn how to make an Alexa skill"



"""
Explanation:
In order to test the Activity suggester class, which imports requests and uses an API to
get datat from the internet,

We need to use our Mocking knowledge to imitate some of the behaviour.

1 - We create an __init__ initializer in the program and assign (requester to self.requester)
-* self.requester.get("website") must be assigned to repsonse in the program

2 - We create a Mock of requester in our test file: This is to imitate part of 
the 'make request' function

3 - We create a response mock, who's purpose is to return the imported request in a readable manner

"""