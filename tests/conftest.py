import os
import pytest
from livedoorblog import LivedoorBlog

def pytest_addoption(parser):
    parser.addoption('--local', action='store_true', help='get environment variables by .env')
    parser.addoption('--username', action='store', help='USERNAME: Livedoor Blog user name')
    parser.addoption('--apikey', action='store', help='APIKEY: Livedoor Blog api key')
    parser.addoption('--blogname', action='store', help='BLOGNAME: Livedoor Blog blog name')

@pytest.fixture(scope='session')
def local(pytestconfig):
    return pytestconfig.option.local

@pytest.fixture(scope='session')
def username(pytestconfig):
    return pytestconfig.option.username

@pytest.fixture(scope='session')
def apikey(pytestconfig):
    return pytestconfig.option.apikey

@pytest.fixture(scope='session')
def blogname(pytestconfig):
    return pytestconfig.option.blogname

@pytest.fixture(scope='session')
def client(local, username, apikey, blogname):
    user_name = os.environ['USER_NAME'] if local else username
    api_key = os.environ['API_KEY'] if local else apikey
    blog_name = os.environ['BLOG_NAME'] if local else blogname
    return LivedoorBlog(user_name, api_key, blog_name)

@pytest.fixture(scope='session')
def client_err():
    return LivedoorBlog('XXXXXXXX', '1234567890')
