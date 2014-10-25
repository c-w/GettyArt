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
    filenames = scraper.scrape(3)

This snippet downloads three paintings to a temporary directory and binds the
locations of the downloaded pieces of art to the filenames variable.

--------------------------------------------------------------------------------

.. image:: http://www.getty.edu/art/collections/images/thumb/00058201-T.JPG

.. image:: http://www.getty.edu/art/collections/images/thumb/00081001-T.JPG

.. image:: http://www.getty.edu/art/collections/images/thumb/00078701-T.JPG

--------------------------------------------------------------------------------

You can also use the scraper from the command line. For instance, the following
command downloads 2 watercolors to your current directory.

.. sourcecode :: sh

    python -m getty_art.getty_art 'Watercolors (paintings)' --limit=2

--------------------------------------------------------------------------------

.. image:: http://www.getty.edu/collection/GRI/thumb/grioc0005428-T.jpg

.. image:: http://www.getty.edu/collection/GRI/thumb/grioc0005417-T.jpg

--------------------------------------------------------------------------------
