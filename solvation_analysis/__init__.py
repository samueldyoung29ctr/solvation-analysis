"""
SolvationAnalysis
An MDAnalysis rmodule for solvation analysis.
"""
from solvation_analysis.solute import Solute

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

from . import _version
__version__ = _version.get_versions()['version']
