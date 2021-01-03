import pytest
import xml.etree.ElementTree as ET
from livedoorblog import LivedoorBlog

def test_initialize():
    client_default = LivedoorBlog('username', 'apikey')
    assert client_default.user_name == 'username'
    assert client_default.api_key == 'apikey'
    assert client_default.blog_name == 'username'

    client_blogname = LivedoorBlog('username2', 'apikey2', 'blogname')
    assert client_blogname.user_name == 'username2'
    assert client_blogname.api_key == 'apikey2'
    assert client_blogname.blog_name == 'blogname'

@pytest.mark.get
def test_get_articles(client, client_err):
    articles = client.get_articles()
    assert articles.status_code == 200

    root = ET.fromstring(articles.text)
    author = root.find('{http://www.w3.org/2005/Atom}author')
    name = author.find('{http://www.w3.org/2005/Atom}name')
    assert name.text == client.user_name

    res_err = client_err.get_articles()
    assert res_err.status_code == 401

@pytest.mark.get
def test_get_article_by_id(client, client_err):
    articles = client.get_articles()
    root = ET.fromstring(articles.text)
    entry = root.find('{http://www.w3.org/2005/Atom}entry')
    link = entry.find('{http://www.w3.org/2005/Atom}link')
    href = link.attrib['href']
    url = f'{client.END_POINT}/{client.blog_name}/article/'
    article_id = href.replace(url, '')

    article = client.get_article_by_id(article_id)
    assert article.status_code == 200

    article_err = client_err.get_article_by_id(article_id)
    assert article_err.status_code == 401

@pytest.mark.get
def test_get_categorys(client, client_err):
    categorys = client.get_categorys()
    assert categorys.status_code == 200

    root = ET.fromstring(categorys.text)
    assert root.tag == '{http://www.w3.org/2007/app}categories'

    categorys_err = client_err.get_categorys()
    assert categorys_err.status_code == 401

@pytest.mark.get
def test_get_images(client, client_err):
    res = client.get_images()
    assert res.status_code == 200

    res_err = client_err.get_images()
    assert res_err.status_code == 403

@pytest.mark.get
def test_get_image_by_id(client, client_err):
    images = client.get_images()
    root = ET.fromstring(images.text)
    entry = root.find('{http://www.w3.org/2005/Atom}entry')
    link = entry.find('{http://www.w3.org/2005/Atom}link')
    href = link.attrib['href']
    url = f'http://livedoor.blogcms.jp/atom/blog/{client.blog_name}/image/'
    image_id = href.replace(url, '')

    image = client.get_image_by_id(image_id)
    assert image.status_code == 200

    image_err = client_err.get_image_by_id(image_id)
    assert image_err.status_code == 401

@pytest.mark.get
def test_get_comments(client, client_err):
    comments = client.get_comments()
    assert comments.status_code == 200

    comments_err = client_err.get_comments()
    assert comments_err.status_code == 403

@pytest.mark.post
def test_post_article(client):
    entry = ET.Element('entry',
                       attrib={
                           'xmlns': 'http://www.w3.org/2005/Atom',
                           'xmlns:app': 'http://www.w3.org/2007/app',
                       })
    title_elm = ET.SubElement(entry, 'title')
    title_elm.text = 'ブログタイトル'
    content_elm = ET.SubElement(entry, 'content', attrib={'type': 'text/html'})
    content_elm.text = 'ブログ内容'
    app_ctrl = ET.SubElement(entry, 'app:control')
    app_draft = ET.SubElement(app_ctrl, 'app:draft')
    app_draft.text = 'yes'
    article = ET.tostring(entry, encoding='utf8', xml_declaration=True)
    res = client.post_article(article)
    assert res.status_code == 201
