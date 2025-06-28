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
pip install mathexpr
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
from mathexpr import MathExpr

math_string = "(2 + 3) * 4^3"
result = MathExpr.evaluate(math_string)
print(result)

>>> 320.0
```
Usage with variables:
```python
from mathexpr import MathExpr
math_string = "x + y"
result = MathExpr.evaluate(math_string, {"x": 2, "y": 3})
print(result)

>>> 5
```
Debug the AST:
```python
from mathexpr import MathExpr, print_ast

math_string = "(2 + 3) * 4^3"
ast = MathExpr.parse(math_string)
print_ast(ast)

>>> TokenType.MUL
>>> ├──TokenType.ADD
>>> │  ├──NumNode(value=2.0)
>>> │  ╰──NumNode(value=3.0)
>>> ╰──TokenType.POW
>>> │  ├──NumNode(value=4.0)
>>> │  ╰──NumNode(value=3.0)
```

## Contributing

If you would like to contribute to this project, please fork the [repository](https://github.com/professionsalincpp/mathexpr) and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/professionsalincpp/mathexpr/blob/main/LICENSE) file for details.

