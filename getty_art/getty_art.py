"""Script to scrape images from getty.edu"""


from __future__ import absolute_import

import itertools
import os
import re
import urllib

from getty_art import util


CATEGORIES = (
    'Architectural drawings',
    'Architecture',
    'Book',
    'Coins',
    'Decorative Arts',
    'Drawings',
    'Figures (illustrations)',
    'Illuminations',
    'Implements',
    'Jewelry',
    'Manuscripts',
    'Mixed Material',
    'Paintings',
    'Photographs',
    'Plates (illustrations)',
    'Playing cards',
    'Prints',
    'Sculpture',
    'Vessels',
    'Visual Material',
    'Watercolors (paintings)',
)


class Scraper(object):
    """Scraper that grabs images from getty.edu.

    Attributes:
        category (str): The category of images to scrape (e.g. Paintings)
        batchsize (int): The number of images to request per query
        page (int): The results page at which to start scraping

    """
    def __init__(self, category, batchsize=100, page=1):
        self._category = category
        self._batchsize = batchsize
        self._page = page

    @classmethod
    def format_filename(cls, url, basedir=None):
        """Creates a local path equivalent to some URL. If `basedir` is not
        specified, the path will be a temporary path.

        Arguments:
            url (str): The remote URL for which to create a local path
            basedir (str, optional): The directory in which to root the path

        Returns:
            str: A local path that is similar to the URL

        """
        basename = os.path.basename(url)
        return (util.tmpfile(basename) if basedir is None
                else os.path.join(util.expandpath(basedir), basename))

    @classmethod
    def extract_images(cls, resultspage):
        """Extracts the URLs for all images on a getty.edu search results page.

        Arguments:
            resultspage (file): A file-handle of a search-result page

        Returns:
            set: The URLs for all images on the page

        """
        image_re = re.compile(r'<a href="(?P<url>[^"]+)" class="cs-enlarge">')
        return set(match.group('url') for line in resultspage
                   for match in image_re.finditer(line))

    def resultspage(self, page):
        """Requests a page of image search results from getty.edu.

        Arguments:
            page (int): The search result page to retrieve

        Returns:
            file: A file-handle for the search results page

        """
        url_template = (r'http://search.getty.edu/gateway/search'
                        r'?q&cat=type&dir=s&img=1'
                        r'&types="{category}"&rows={batchsize}&pg={page}')
        url = url_template.format(
            category=self._category,
            batchsize=self._batchsize,
            page=page)
        return urllib.urlopen(url)

    def scrape(self, num=None, basedir=None):
        """Scrapes and downloads images from getty.edu to a local directory.

        Arguments:
            num (int): The number of images to scrape
            basedir (str): The directory at which to store the images

        Returns:
            list: The paths of all the scraped images

        """
        filenames = []
        for image_url in itertools.islice(self, num):
            filename = self.format_filename(image_url, basedir)
            urllib.urlretrieve(image_url, filename)
            filenames.append(filename)
        return filenames

    def __iter__(self):
        """Iteratively finds all the URLs to the images on getty.edu in the
        category that the scraper is targeting.

        Yields:
            str: The URL to a getty.edu image

        """
        while True:
            resultspage = self.resultspage(self._page)
            image_urls = self.extract_images(resultspage)
            if image_urls:
                for image_url in image_urls:
                    yield image_url
                self._page += 1
            else:
                break


def _main():
    """Command line interface to the module.

    """
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('category', metavar='category', choices=CATEGORIES,
                        help=('type of images to scrape; '
                              'allowed values are: ' + ', '.join(CATEGORIES)))
    parser.add_argument('-l', '--limit', metavar='L', default=None, type=int,
                        help='maximum number of images to scrape')
    parser.add_argument('-o', '--output', metavar='O', default='.',
                        help='directory in which to store images')
    parser.add_argument('-p', '--page', metavar='P', default=1,
                        help='results page at which to start scraping')
    parser.add_argument('--batchsize', metavar='B', default=100,
                        help='number of results to fetch per query')
    args = parser.parse_args()

    Scraper(
        category=args.category,
        batchsize=args.batchsize,
        page=args.page,
    ).scrape(
        num=args.limit,
        basedir=args.output,
    )


if __name__ == '__main__':
    _main()
