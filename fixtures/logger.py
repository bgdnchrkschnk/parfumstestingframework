import logging
from io import StringIO

import allure
import pytest

@pytest.fixture
def custom_logger(request):
    custom_logger = logging.getLogger(request.function.__name__)
    custom_logger.setLevel(level=logging.DEBUG)
    string_io = StringIO()

    # Create console streaming handler
    c_handler = logging.StreamHandler()

    # Creating string io streaming handler
    s_handler = logging.StreamHandler(stream=string_io)

    # Create formatters for each handler
    c_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    s_handler_format = logging.Formatter('%(asctime)s == %(process)d == %(name)s == %(levelname)s: %(message)s')

    # Set formatters for handlers
    c_handler.setFormatter(c_handler_format)
    s_handler.setFormatter(s_handler_format)

    # Add handlers to our logger objects
    custom_logger.addHandler(c_handler)
    custom_logger.addHandler(s_handler)

    yield custom_logger

    allure.attach(string_io.getvalue(), name="Log file", attachment_type=allure.attachment_type.TEXT)
