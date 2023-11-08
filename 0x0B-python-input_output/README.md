# Python Input and Output Functions

This repository contains a collection of Python functions designed to make input and output operations easier and more efficient in your Python projects. These functions can help streamline your code and enhance the user experience of your applications.

## Table of Contents

- [Functions](#functions)
  - [Input Functions](#input-functions)
  - [Output Functions](#output-functions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Functions

### Input Functions

1. `input_integer(prompt: str) -> int`: A function to safely take an integer input from the user, displaying a custom prompt.

2. `input_float(prompt: str) -> float`: Get a floating-point number from the user with a custom prompt.

3. `input_string(prompt: str) -> str`: Receive a string input with a customized prompt.

### Output Functions

1. `print_title(title: str)`: Print a stylized title to the console to enhance the appearance of your application.

2. `print_list(items: list, title: str)`: Display a list of items, optionally with a title.

3. `save_to_file(data: str, filename: str)`: Write data to a file with a specified filename.

## Usage

1. Clone or download this repository to your local machine.

2. Import the desired input or output functions into your Python project using the `from` and `import` syntax, for example:

   ```python
   from input_output_functions import input_integer, print_title

