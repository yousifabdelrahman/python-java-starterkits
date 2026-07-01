"""Tests for python_java_starterkits."""

from python_java_starterkits import PythonJavaStarterkits, PythonJavaStarterkitsOptions


class TestPythonJavaStarterkits:
    def test_create_instance_with_defaults(self) -> None:
        instance = PythonJavaStarterkits()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = PythonJavaStarterkitsOptions(verbose=True)
        instance = PythonJavaStarterkits(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = PythonJavaStarterkits()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = PythonJavaStarterkits()
        result = instance.run()
        assert result.error is None
