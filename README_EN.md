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

- [TIN United States](#tin_united_states_of_america)
  - [remove\_symbols](#remove_symbols)
  - [is\_valid\_ssn](#is_valid_ssn)
  - [is\_valid\_ein](#is_valid_ein)
  - [format\_ssn](#format_ssn)
  - [format\_ein](#format_ein)
  - [generate\_ssn](#generate_ssn)
  - [generate\_ein](#generate_ein)
  - [example\_usage](#example_usage)


## TIN United States


### remove_symbols

Remove spaces, dots, and hyphens from the input string.

Args:

- tin (str): The TIN to be validated, a string of 9 digits (numbers).

Returns:

- bool: True if the checksum digits match the base number,
          False otherwise.


### is_valid_ssn

Social Security Number (SSN) - Validates the TIN of the ssn (citizen/ssn) to ensure that it is within the country specifications passed as parameters!

Args:

- tin (str): A string with 9 digits.

Returns:

- str: If the input passed by the user contains anything other than the above argument, return an "invalid" error message.

Example:

```python
>>> from tin_united_states_of_america import is_valid_ssn
>>> is_valid_ssn("123 45 6789") => 'Valid United States TIN'
>>> is_valid_ssn("1230 456 789") => 'Invalid United States TIN'
```


### is_valid_ein

Employer Identification Number (EIN) - Validates the TIN of the legal entity (EIN) to ensure that it is within the specifications of the country passed as parameters!

Arguments:

- tin (str): A string with 9 digits.

Returns:

- str: If the input passed by the user contains anything other than the argument above, returns an "invalid" error message.

Example:

```python
>>> from tin_united_states_of_america import is_valid_ein
>>> is_valid_ein("12-3456789") => 'Valid United States TIN'
>>> is_valid_ein("120-3456789") => 'Invalid United States TIN'
```


### format_ssn

Social Security Number (SSN) - Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

```python
>>> from tin_united_states_of_america import format_ssn
>>> format_ssn("123456789") => ("123 45 6789")
```


### format_ein

Employer Identification Number (EIN) - Formats an TIN for display.

Args:

- tin(str): Adds the correct separators as per the country parameters.

Returns:

- str: A formatted TIN with the separators in the right place!

Example:

Exemplo:
```python
>>> from tin_united_states_of_america import format_ein
>>> format_ein("123456789") => ("12-3456789")
```


### generate_ssn

Social Security Number (SSN) - Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_united_states_of_america import generate_ssn
>>> generate_ssn("123 45 6789") => 'Valid United States TIN'
>>> generate_ssn("1230 456 789") => 'Invalid United States TIN'
```


### generate_ein

Employer Identification Number (EIN) - Generates a valid TIN.

Args:

- tin (str): Generates a valid TIN.

Returns:

- str: Generates a valid number given the correct parameters.

Example:

```python
>>> from tin_united_states_of_america import generate_ein
>>> generate_ein("12-3456789") => 'Valid United States TIN'
>>> generate_ein("120-3456789") => 'Invalid United States TIN'
```


### example_usage

Generates random valid TIN as an example for ssns and legal entities, analyzes user input, and formats them.

Arguments:

- str: A valid randomly generated TIN as an example for ssns and companies, user input.

Returns:

- str: A valid randomly generated TIN as an example for ssns and companies, user input parsed and formatted with visual symbols if valid, None if not.

Example:

```python
>>> from tin_united_states_of_america import example_usage
>>> tin_ssn("123456789") => 'Valid United States TIN ssn'
>>> tin_ein("123456789") => 'Valid United States TIN ein'

>>> is_valid(tin_ssn) => 'Valid United States TIN ein'
>>> is_valid(tin_ein) => 'Valid United States TIN ein'

>>> is_valid(user_input)("254789654") => 'Valid input - United States TIN ein'

>>> formatted_input = format_tin(user_input) => ("25-4789654")
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
