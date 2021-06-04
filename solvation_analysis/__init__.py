"""
SolvationAnalysis
An MDAnalysis rmodule for solvation analysis.
"""

# Add imports here
from .solvation import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
