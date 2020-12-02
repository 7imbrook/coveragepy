# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

"""A plugin for tests to reference."""

from coverage4 import CoveragePlugin


class Plugin(CoveragePlugin):
    pass


def coverage_init(reg, options):
    reg.add_file_tracer(Plugin())
