# MathExpr

MathExpr is a Python library for parsing and evaluating mathematical expressions.

## Table of Contents

* [Getting Started](#getting-started)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Getting Started

To get started with this project, please follow these steps:

### Prerequisites

* Python 3.8+
* pip 20.0+

### Installation

To install the library, run the following command:
```bash
pip install mathparse
```

## Features

MathExpr provides the following features:

* Parsing mathematical expressions
* Evaluating mathematical expressions
* Evaluating mathematical expressions with variables

## Usage

To use MathExpr, import the `MathParse` class and use the `parse` and `evaluate` methods.
Simple usage example:
```python
from mathexpr import MathParse

math_string = "(2 + 3) * 4^3"
result = MathParse.evaluate(math_string)
```
Usage with variables:
```python
from mathexpr import MathParse

math_string = "x + y"
result = MathParse.evaluate(math_string, {"x": 2, "y": 3})
```

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/professionsalincpp/mathparse/blob/main/mathparse/LICENSE) file for details.

