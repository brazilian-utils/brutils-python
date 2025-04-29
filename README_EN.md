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

# Utilities

- [TIN Anguilla](#tin_anguilla)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid\_individual](#is_valid_individual)
  - [is\_valid\_company](#is_valid_company)
  - [is\_valid](#is_valid)
  - [format\_tin](#format_tin)
  - [generate](#generate)
  - [example\_usage](#example_usage)


## TIN Anguilla


### remove_symbols

Remove spaces, dots, and hyphens from the input string.

Args:

- tin (str): The TIN to be validated, a string of 10 to 12 digits (letters and numbers).

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.


### is_valid_individual

Validates the TIN of the individual (citizen/individual) to ensure that it is within the country specifications passed as parameters!

Args:

- tin (str): A string with 10 characters, the first 2 being letters and the rest being digits.

Returns:

- str: If the input passed by the user contains anything other than the above argument, return an "invalid" error message.

Example:

```python
>>> from tin_anguilla import is_valid_individual
>>> is_valid_individual("AB12345678") => 'Valid Anguilla TIN'
>>> is_valid_individual("XYZ1234567") => 'Invalid Anguilla TIN: Must start with two letters.'
```


### is_valid_company

Validates the TIN of the legal entity (company) to ensure that it is within the specifications of the country passed as parameters!

Arguments:

- tin (str): A string between 10 and 12 characters, the first 3 being letters and the remaining digits.

Returns:

- str: If the input passed by the user contains anything other than the argument above, returns an "invalid" error message.

Example:

```python
>>> from tin_anguilla import is_valid_company
>>> is_valid_company("ABC12345678") => 'Valid Anguilla TIN'
>>> is_valid_company("XY1234567") => 'Invalid Anguilla TIN: Must start with three letters.'
```


### is_valid

Determines whether the TIN is valid for individuals or legal entities.

Returns:

- str: If the input is equal to 10 digits, it is individual. If it is greater than 10 (up to 12) it is for a company.

Example:

```python
>>> from tin_anguilla import is_valid
>>> is_valid("AB12345678") => 'Valid Anguilla TIN Individual'
>>> is_valid("XYZ12345678") => 'Valid Anguilla TIN Company'
```

### format_tin

Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

```python
>>> from tin_anguilla import format_tin
>>> format_tin("GEH15998436") => ("GEH-15998436")
```


### generate

Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_anguilla import generate
>>> generate("AB12345678") => 'Valid Anguilla TIN Individual'
>>> generate("XYZ12345678") => 'Valid Anguilla TIN Company'
```


### example_usage

Generates random valid TIN as an example for individuals and legal entities, analyzes user input, and formats them.

Arguments:

- str: A valid randomly generated TIN as an example for individuals and companies, user input.

Returns:

- str: A valid randomly generated TIN as an example for individuals and companies, user input parsed and formatted with visual symbols if valid, None if not.

Example:

```python
>>> from tin_anguilla import example_usage
>>> tin_individual("AB12345678") => 'Valid Anguilla TIN Individual'
>>> tin_company("XYZ12345678") => 'Valid Anguilla TIN Company'

>>> is_valid(tin_individual) => 'Valid Anguilla TIN Company'
>>> is_valid(tin_company) => 'Valid Anguilla TIN Company'

>>> is_valid(user_input)("GEH15998436") => 'Valid input - Anguilla TIN Company'

>>> formatted_input = format_tin(user_input) => ("GEH-15998436")
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
