# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""Code coverage measurement for Python.

Ned Batchelder
https://nedbatchelder.com/code/coverage

"""

import sys

from coverage5.version import __version__, __url__, version_info

from coverage5.control import Coverage, process_startup
from coverage5.data import CoverageData
from coverage5.misc import CoverageException
from coverage5.plugin import CoveragePlugin, FileTracer, FileReporter
from coverage5.pytracer import PyTracer

# Backward compatibility.
coverage5 = Coverage

# On Windows, we encode and decode deep enough that something goes wrong and
# the encodings.utf_8 module is loaded and then unloaded, I don't know why.
# Adding a reference here prevents it from being unloaded.  Yuk.
import encodings.utf_8  # pylint: disable=wrong-import-position, wrong-import-order

# Because of the "from coverage5.control import fooey" lines at the top of the
# file, there's an entry for coverage.coverage in sys.modules, mapped to None.
# This makes some inspection tools (like pydoc) unable to find the class
# coverage.coverage.  So remove that entry.
try:
    del sys.modules["coverage5.coverage5"]
except KeyError:
    pass
