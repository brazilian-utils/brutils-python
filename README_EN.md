<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Procurando pela versão em português?](README.md)

</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in
the development of applications for the Brazilian business.

- [Installation](#installation)
- [Usage](#usage)
- [Utilities](#utilities)
- [Feature Request and Bug Report](#feature-request-and-bug-report)
- [Questions? Ideas?](#questions-ideas)
- [Code Contribution](#code-contribution)

# Installation

```bash
pip install brutils
```

# Usage

To use one of our utilities you just need to import the required function as in the example below:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```


- [TIN Venezuela](#tin_venezuela)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid](#is_valid)
  - [\_calculate\_digit](#_calculate_digit)
  - [format\_tin](#format_tin)
  - [generate](#generate)
  - [example\_usage](#example_usage)

## TIN Venezuela

### remove_symbols

Remove spaces, dots, and hyphens from the input string.

Args:

- tin (str): The TIN (NIF) to be validated, a string starting with a letter, followed by 8 numbers and a check digit.

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.


### is_valid

Validates the TIN to ensure that it is within the country specifications passed as parameters!

Args:

- tin (str): A string with 10 digits.

Returns:

- str: If the input passed by the user contains anything other than the above argument, return an "invalid" error message.

Example:

```python
>>> from tin_venezuela import is_valid
>>> is_valid("V-12345678-9") => 'Valid Venezuela TIN'
>>> is_valid("A-12345678-9") => 'Invalid Venezuela TIN'
```


### format_tin

Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

```python
>>> from tin_venezuela import format_tin
>>> format_tin("V123456789") => ("V-12345678-9")
```

### generate

Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_venezuela import generate
>>> generate("V-12345678-9") => 'Valid Venezuela TIN'
>>> generate("A-12345678-9") => 'Invalid Venezuela TIN'
```


### example_usage

Generates random valid TIN as an example, analyzes user input, and formats them.

Arguments:

- str: A valid randomly generated TIN, user input.

Returns:

- str: A valid randomly generated TIN as an example, user input parsed and formatted with visual symbols if valid, None if not.

Example:

```python
>>> from tin_venezuela import example_usage
>>> tin("E784532186") => 'Valid Venezuela TIN'

>>> is_valid(tin) => 'Valid Venezuela TIN'

>>> is_valid(user_input)("E784532186") => 'Valid input - Venezuela TIN'

>>> formatted_input = format_tin(user_input) => ("E-78453218-6")
```

---

# Feature Request and Bug Report

If you want to suggest new features or report bugs, simply create
a new [issue][github-issues], and we will respond to you there!

(To learn more about GitHub issues, check out the [official GitHub documentation][github-issues-doc]).

# Questions? Ideas?

Questions on how to use the library? New ideas for the project?
Want to share something with us? Feel free to start a thread in our
[Discussions][github-discussions], and we'll interact with you there!

(To learn more about GitHub discussions, refer to the
[official GitHub documentation][github-discussions-doc]).

# Code Contribution

Your collaboration is always very welcome! We've prepared the [CONTRIBUTING.md][contributing] file
to assist you in getting started. There, you'll find all the information you need to contribute to
the project. Please, don't hesitate to ask us using [GitHub Discussions][github-discussions] if
you encounter any difficulties or have any questions. Every bit of help counts!

Let's build it together 🚀🚀

[contributing]: CONTRIBUTING_EN.md
[github-discussions-doc]: https://docs.github.com/en/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues

## ❤️ Contributors

<a href="https://github.com/brazilian-utils/brutils-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brazilian-utils/brutils-python" />
</a></br></br>

_Made with [contrib.rocks](https://contrib.rocks)._
