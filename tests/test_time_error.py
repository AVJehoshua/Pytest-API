from unittest.mock import *
from lib.time_error import *

"""
Purpose of time error is to return difference in seconds between 
time on external srever, and on this computer

When we call def error(), it returns this difference

When we call get_server_time(), it requests server time from API website,
turns that data into son file so more readable
and we return from that json file, the value from key'unixtime'

In order to test this, i'll want to create a mock of requests and response, to
create a controlled return value of unixtime, and a controlled time
"""

"""
When we call error(), 
it returns the difference between server time and computer time
"""

def test_difference_between_servers():
    mock_requester = Mock()
    mock_response = Mock()
    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {"unixtime": 1700921556}
    mock_timer = Mock()
    mock_timer.time.return_value = 1700921556.5
    time_error = TimeError(mock_requester, mock_timer)
    assert time_error.error() == -0.5


"""
Explanation:

Created Mocks of requester, response and timer - as these are the values we wish to determine
and keep consistent

Followed process of assigining mock response as the mock requester return value

Made ge mock_repsonse json return value a dict of our expected key from the URL

For time:

We created timer mock, and created self.timer initializer within __init__()

assigned the return value to time.time() *got this from calling time.time() in python terminal)

We added mock_timer as an an argument when calling TimerError() class

We asserted the result to be -0.5, 
minuis, as the return value kept being a return number
.5, as this is easy to work with when dealing with floats
"""
