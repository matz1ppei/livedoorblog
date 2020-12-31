import os
import pytest
from livedoorblog import LivedoorBlog

@pytest.fixture(scope='session')
def client(pytestconfig):
    user_name = os.environ['USER_NAME']
    api_key = os.environ['API_KEY']
    blog_name = os.environ['BLOG_NAME']
    return LivedoorBlog(user_name, api_key, blog_name)

@pytest.fixture(scope='session')
def client_err():
    return LivedoorBlog('XXXXXXXX', '1234567890')
