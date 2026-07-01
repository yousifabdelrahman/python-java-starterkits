# python_java_starterkits

Generate paired Python and Java starter projects with the same problem and tests.

## Installation

```bash
pip install python_java_starterkits
```

## Quick Start

```python
from python_java_starterkits import PythonJavaStarterkits

instance = PythonJavaStarterkits()
result = instance.run()
print(result)
```

## Features

- CLI to scaffold matching Python and Java projects
- Shared spec file that defines exercises, inputs, and expected outputs
- Auto-generated unit tests (pytest + JUnit)
- GitHub-ready structure with README and tasks checklist

## API Reference

### `PythonJavaStarterkits`

#### Constructor

```python
PythonJavaStarterkits(options: PythonJavaStarterkitsOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `PythonJavaStarterkitsResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/python_java_starterkits/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
