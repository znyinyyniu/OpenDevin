import os

from litellm import completion

from tests.integration.conftest import get_mock_response


def mock_completion(*args, **kwargs):
    test_name = 'test_write_simple_script'
    os.environ['AGENT'] = 'CodeActAgent'

    messages = kwargs['messages']
    message_str = ''
    for message in messages:
        message_str += message['content']
    mock_response = get_mock_response(test_name, message_str, 0)
    response = completion(**kwargs, mock_response=mock_response)
    return response
