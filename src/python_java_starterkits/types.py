"""Type definitions for python_java_starterkits."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class PythonJavaStarterkitsOptions:
    """Configuration options for PythonJavaStarterkits.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: CLI to scaffold matching Python and Java projects
        feature_2: Configuration for: Shared spec file that defines exercises, inputs, and expected outputs
        feature_3: Configuration for: Auto-generated unit tests (pytest + JUnit)
        feature_4: Configuration for: GitHub-ready structure with README and tasks checklist
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None


@dataclass
class PythonJavaStarterkitsResult:
    """Result returned by PythonJavaStarterkits operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
