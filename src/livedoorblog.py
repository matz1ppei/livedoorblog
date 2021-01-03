from base64 import b64encode
from datetime import datetime
from hashlib import sha1
from uuid import uuid4
import requests
from requests.auth import HTTPBasicAuth

class LivedoorBlog:

    END_POINT = 'https://livedoor.blogcms.jp/atompub'
    END_POINT_OLD = 'https://livedoor.blogcms.jp/atom/blog'

    def __init__(self, user_name, api_key, blog_name=None):
        self.__user_name = user_name
        self.__api_key = api_key
        self.__blog_name = blog_name if blog_name is not None else user_name

    @property
    def user_name(self):
        return self.__user_name

    @property
    def api_key(self):
        return self.__api_key

    @property
    def blog_name(self):
        return self.__blog_name

    def __create_wsse(self):
        nonce = uuid4().hex
        created = datetime.now().isoformat() + 'Z'
        digest = b64encode(sha1((nonce + created + self.__api_key).encode()).digest()).decode()
        return f'UsernameToken Username="{self.__user_name}", PasswordDigest="{digest}", Nonce="{nonce}", Created="{created}"'

    def __get(self, url):
        auth = HTTPBasicAuth(self.__user_name, self.__api_key)
        return requests.get(url, auth=auth)

    def __get_with_old_api(self, url):
        wsse = self.__create_wsse()
        return requests.get(url, headers={'X-WSSE': wsse})

    def get_articles(self):
        url = f'{LivedoorBlog.END_POINT}/{self.__blog_name}/article'
        return self.__get(url)

    def get_article_by_id(self, article_id):
        url = f'{LivedoorBlog.END_POINT}/{self.__blog_name}/article/{article_id}'
        return self.__get(url)

    def get_categorys(self):
        url = f'{LivedoorBlog.END_POINT}/{self.__blog_name}/category'
        return self.__get(url)

    def get_images(self):
        url = f'{LivedoorBlog.END_POINT_OLD}/{self.__blog_name}/image'
        return self.__get_with_old_api(url)

    def get_image_by_id(self, image_id):
        url = f'{LivedoorBlog.END_POINT}/{self.__blog_name}/image/{image_id}'
        return self.__get(url)

    def get_comments(self):
        url = f'{LivedoorBlog.END_POINT_OLD}/{self.__blog_name}/comment'
        return self.__get_with_old_api(url)

    def get_comment_by_id(self, comment_id):
        url = f'{LivedoorBlog.END_POINT_OLD}/{self.__blog_name}/comment/{comment_id}'
        return self.__get_with_old_api(url)

    def post_article(self, article):
        url = f'{LivedoorBlog.END_POINT}/{self.__blog_name}/article'
        auth = HTTPBasicAuth(self.__user_name, self.__api_key)
        headers = {'Content-Type': 'application/atom+xml;type=entry'}
        return requests.post(url, data=article, headers=headers, auth=auth)
