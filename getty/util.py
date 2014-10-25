"""Module for helper functions."""


import os
import tempfile


def tmpfile(suffix='', prefix='tmp', directory=None):
    """Wrapper around tempfile.mkstemp that creates a new temporary file path.

    """
    filehandle, filename = tempfile.mkstemp(suffix, prefix, directory)
    os.close(filehandle)
    return filename
