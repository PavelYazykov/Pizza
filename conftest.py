import logging.config
import pytest
import logging
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'login.ini')
logging.config.fileConfig(log_file_path)
