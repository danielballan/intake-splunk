from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .core import SplunkSource
from .core import SplunkConnect
