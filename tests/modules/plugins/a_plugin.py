"""A plugin for tests to reference."""

from coverage4 import CoveragePlugin


class Plugin(CoveragePlugin):
    pass


def coverage_init(reg, options):
    reg.add_file_tracer(Plugin())
