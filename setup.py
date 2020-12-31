from setuptools import setup, find_packages

setup(
    name='livedoorblog',
    version='0.0.1',
    description='Livedoor Blog API Client',

    author='Ippei Matsubara',
    author_email='matz1ppei@gmail.com',
    url='',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['requests'],
    tests_requires=['pytest']
)
