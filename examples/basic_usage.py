#!/usr/bin/env python3
"""Basic usage example for python_java_starterkits."""

from python_java_starterkits import PythonJavaStarterkits, PythonJavaStarterkitsOptions


def main() -> None:
    # Create with default options
    instance = PythonJavaStarterkits()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = PythonJavaStarterkitsOptions(verbose=True)
    instance = PythonJavaStarterkits(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
