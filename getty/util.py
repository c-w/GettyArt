# pylint:disable=C0111
import os
import tempfile


def tmpfile(suffix='', prefix='tmp', directory=None):
    filehandle, filename = tempfile.mkstemp(suffix, prefix, directory)
    os.close(filehandle)
    return filename
