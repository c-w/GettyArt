********
GettyArt
********


Overview
========

This package contains a scraper for Art!

The *getty_art* package uses the search API of the `Getty Museum
<http://www.getty.edu>`_ to deliver the finest art directly to a local drive
near to you.


Usage
=====

Grabbing some fine art using this package is super simple:

.. sourcecode :: py

    import getty_art

    scraper = getty_art.Scraper(category='Paintings')
    filenames = scraper.scrape(5)

This snippet downloads five paintings to a temporary directory and binds the
locations of the downloaded pieces of art to the filenames variable.

You can also use the scraper from the command line. For instance, the following
command downloads 10 watercolors to your current directory.

.. sourcecode :: sh

    python -m getty_art.getty_art 'Watercolors (paintings)' --limit=10
