from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='livedoorblog',
    version='0.0.3',
    description='Livedoor Blog API Client for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ippei Matsubara',
    author_email='matz1ppei@gmail.com',
    url='https://github.com/matz1ppei/livedoorblog',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['requests'],
    tests_require=['pytest', 'pytest-cov']
)
