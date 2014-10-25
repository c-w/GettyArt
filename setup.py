from distutils.core import setup

setup(
    name='Getty Art',
    version='0.0.1',
    author='Clemens Wolff',
    author_email='clemens.wolff+pypi@gmail.com',
    packages=['getty_art'],
    url='https://github.com/c-w/GettyArt',
    download_url='http://pypi.python.org/pypi/GettyArt',
    license='LICENSE.txt',
    description='Scraper for art available from getty.edu',
    long_description=open('README.rst').read(),
)