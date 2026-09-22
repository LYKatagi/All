# all

> A general-purpose Python library with useful tools for everyday programming.

`all` is a Python library designed to bring commonly needed utilities into a single, simple and consistent package.

The goal is to provide useful functionality for areas such as mathematics, strings, files, system information, networking and more.

## Features

* 🧮 Mathematics utilities
* 🔤 String utilities
* 📁 File utilities
* 💻 System utilities
* 🌐 Network utilities
* 🛠️ General-purpose helpers
* 🧪 Tests for the library
* 📦 Installable as a Python package

## Installation

```bash
pip install all
```

## Usage

```python
import all

print(all.math.clamp(150, 0, 100))
```

Or import specific modules:

```python
from all import math, strings

print(math.clamp(150, 0, 100))
print(strings.reverse("Hello, world!"))
```

## Project Structure

```text
all/
├── src/
│   └── all/
│       ├── __init__.py
│       ├── math.py
│       ├── strings.py
│       ├── files.py
│       ├── system.py
│       ├── network.py
│       └── utils.py
│
├── tests/
├── examples/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## Development

Clone the repository:

```bash
git clone <repository-url>
cd all
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

## Testing

Run the test suite with:

```bash
python -m pytest
```

## Philosophy

`all` aims to be:

* **Simple** — easy to learn and use.
* **Useful** — focused on practical functionality.
* **Consistent** — similar APIs across modules.
* **Portable** — designed to work across platforms whenever possible.
* **Extensible** — easy to expand with new modules.

The library should grow based on useful functionality rather than simply trying to contain every possible feature.

## License

This project is licensed under the terms of the license included in this repository.
