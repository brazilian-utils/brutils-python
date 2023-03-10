# Contributing

Thanks for taking the time to contribute! 🙇‍♀️🙇‍♂️ Every little bit of help counts!

## Installation
### Requirements
- [Python 3.7+][python]
- [Poetry][poetry]

Fork or clone the repository and enter into the project's folder:

```shell
$ git clone git@github.com:brazilian-utils/brutils-python.git
$ cd brutils-python
```

Create a [virtualenv][virtualenv] for ScanAPI and activate it:

```shell
$ make shell
```

**Note: You need to run `make shell` every time you open a new terminal window/tab.**

Install the dependencies:

```shell
$ make install
```

## Using locally

```shell
$ make run-python
```

Now, you can use it [in the same way described in the README.md file](/README.md#usage)

## Tests

```shell
$ make test
```

[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
