"""
python_java_starterkits - Generate paired Python and Java starter projects with the same problem and tests.
"""

__version__ = "0.1.0"

from .cli_to_scaffold_matching_pytho import PythonJavaStarterkits
from .types import PythonJavaStarterkitsOptions, PythonJavaStarterkitsResult
from .exceptions import PythonJavaStarterkitsError, ConfigurationError, ValidationError

__all__ = [
    "PythonJavaStarterkits",
    "PythonJavaStarterkitsOptions",
    "PythonJavaStarterkitsResult",
    "PythonJavaStarterkitsError",
    "ConfigurationError",
    "ValidationError",
]
