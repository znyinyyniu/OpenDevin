import os

from tests.integration.conftest import mock_completion as mc


def mock_completion(*args, **kwargs):
    test_name = 'test_write_simple_script'
    os.environ['AGENT'] = 'MonologueAgent'
    return mc(*args, test_name=test_name, **kwargs)
