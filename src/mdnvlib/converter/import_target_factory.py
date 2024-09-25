"""Provide a factory class for a novx file object to write.

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/mdnvlib
License: GNU LGPLv3 (https://www.gnu.org/licenses/lgpl-3.0.en.html)
"""
import os

from mdnvlib.converter.file_factory import FileFactory
from mdnvlib.novx_globals import Error
from mdnvlib.novx_globals import _


class ImportTargetFactory(FileFactory):
    """A factory class that instantiates a novx file object to write."""

    def make_file_objects(self, sourcePath, **kwargs):
        """Instantiate a target object for conversion to a mdnovel project.

        Positional arguments:
            sourcePath: str -- path to the source file to convert.

        Required keyword arguments: 
            suffix: str -- target file name suffix.

        Return a tuple with two elements:
        - sourceFile: None
        - targetFile: a NovxFile subclass instance

        Raise the "Error" exception in case of error. 
        """
        fileName, __ = os.path.splitext(sourcePath)
        sourceSuffix = kwargs['suffix']
        if sourceSuffix:
            # Remove the suffix from the source file name.
            # This should also work if the file name already contains the suffix,
            # e.g. "test_notes_notes.odt".
            e = fileName.split(sourceSuffix)
            if len(e) > 1:
                e.pop()
            ywPathBasis = ''.join(e)
        else:
            ywPathBasis = fileName

        # Look for an existing mdnovel project to rewrite.
        for fileClass in self._fileClasses:
            if os.path.isfile(f'{ywPathBasis}{fileClass.EXTENSION}'):
                targetFile = fileClass(f'{ywPathBasis}{fileClass.EXTENSION}', **kwargs)
                return None, targetFile

        raise Error(f'{_("No mdnovel project to write")}.')
