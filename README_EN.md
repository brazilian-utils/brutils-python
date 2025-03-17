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

- [TIN Australia](#tin_Australia)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid\_tfn](#is_valid_tfn)
  - [is\_valid\_abn](#is_valid_abn)
  - [format\_tfn](#format_tfn)
  - [format\_abn](#format_abn)
  - [generate\_tfn](#generate_tfn)
  - [generate\_abn](#generate_abn)
  - [example\_usage](#example_usage)


## TIN Australia


### remove_symbols

Remove spaces, dots, and hyphens from the input string.

Args:

- tin (str): The TIN to be validated, a string of 8 to 11 digits (numbers).

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.


### is_valid_tfn

Australian Tax File Number (TFN) - Validates the TIN of the tfn (citizen/tfn) to ensure that it is within the country specifications passed as parameters!

Args:

- tin (str): A string with 8 or 9 digits (1 check digit).

Returns:

- str: If the input passed by the user contains anything other than the above argument, return an "invalid" error message.

Example:

```python
>>> from tin_Australia import is_valid_tfn
>>> is_valid_tfn("123 456 789") => 'Valid Australia TIN'
>>> is_valid_tfn("1230 456 789") => 'Invalid Australia TIN'
```


### is_valid_abn

Australian Business Number (ABN) - Validates the TIN of the legal entity (abn) to ensure that it is within the specifications of the country passed as parameters!

Arguments:

- tin (str): A string with 11 digits (2 check digit).

Returns:

- str: If the input passed by the user contains anything other than the argument above, returns an "invalid" error message.

Example:

```python
>>> from tin_Australia import is_valid_abn
>>> is_valid_abn("12 345 678 901") => 'Valid Australia TIN'
>>> is_valid_abn("120 345 678 901") => 'Invalid Australia TIN'
```


### format_tfn

Australian Tax File Number (TFN) - Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

```python
>>> from tin_Australia import format_tfn
>>> format_tfn("123456789") => ("123 456 789")
```


### format_abn

Australian Business Number (ABN) - Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

```python
>>> from tin_Australia import format_abn
>>> format_abn("12345678901") => ("12 345 678 901")
```


### generate_tfn

Australian Tax File Number (TFN) - Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_Australia import generate_tfn
>>> generate_tfn("123 456 789") => 'Valid Australia TIN'
>>> generate_tfn("1230 456 789") => 'Invalid Australia TIN'
```


### generate_abn

Australian Business Number (ABN) - Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_Australia import generate_abn
>>> generate_abn("12 345 678 901") => 'Valid Australia TIN'
>>> generate_abn("120 345 678 901") => 'Invalid Australia TIN'
```


### example_usage

Generates random valid TIN as an example for tfns and legal entities, analyzes user input, and formats them.

Arguments:

- str: A valid randomly generated TIN as an example for tfns and companies, user input.

Returns:

- str: A valid randomly generated TIN as an example for tfns and companies, user input parsed and formatted with visual symbols if valid, None if not.

Example:

```python
>>> from tin_Australia import example_usage
>>> tin_tfn("123456789") => 'Valid Australia TIN tfn'
>>> tin_abn("12345678901") => 'Valid Australia TIN abn'

>>> is_valid(tin_tfn) => 'Valid Australia TIN abn'
>>> is_valid(tin_abn) => 'Valid Australia TIN abn'

>>> is_valid(user_input)("36485987125") => 'Valid input - Australia TIN abn'

>>> formatted_input = format_tin(user_input) => ("36 485 987 125")
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
