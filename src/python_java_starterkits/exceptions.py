"""Custom exceptions for python_java_starterkits."""

from __future__ import annotations


class PythonJavaStarterkitsError(Exception):
    """Base exception for all PythonJavaStarterkits errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(PythonJavaStarterkitsError):
    """Raised when the SDK is misconfigured."""


class ValidationError(PythonJavaStarterkitsError):
    """Raised when input validation fails."""


class TimeoutError(PythonJavaStarterkitsError):
    """Raised when an operation exceeds its time limit."""
