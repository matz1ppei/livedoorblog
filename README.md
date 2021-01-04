# livedoorblog
[![CircleCI](https://circleci.com/gh/matz1ppei/livedoorblog.svg?style=svg)](https://circleci.com/gh/matz1ppei/livedoorblog)  

Livedoor Blog API Client for Python

## Dependencies
・requests


## Install

```bash
pip install livedoorblog
```

## Usage
```python
from livedoorblog import LivedoorBlog

LB = LivedoorBlog('<USER_NAME>', '<API_KEY>')

```
## Function
### get articles
```python
articles = LB.get_articles()
```
### get categorys
```python
categorys = LB.get_categorys()
```

## Developer
```python
pytest
```
