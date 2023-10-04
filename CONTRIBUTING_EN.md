# Contributing

Thanks for taking the time to contribute! 🙇‍♀️🙇‍♂️ Every little bit of help counts!

- [First Contribution](#first-contribution)
- [Release a New Version](#release-a-new-version)

# First Contribution

How to make your first contribution:

- [1. Create a GitHub Account](#1-create-a-github-account)
- [2. Find an Issue to Work With](#2-find-an-issue-to-work-with)
- [3. Install Git](#3-install-git)
- [4. Fork the Project](#4-fork-the-project)
- [5. Clone your Fork](#5-clone-your-fork)
- [6. Create a New Branch](#6-create-a-new-branch)
- [7. Run brutils locally](#7-run-brutils-locally)
- [8. Make your changes](#8-make-your-changes)
- [9. Test your changes](#9-test-your-changes)
- [10. Commit and push your changes](#10-commit-and-push-your-changes)
- [11. Add changelog entries](#11-add-changelog-entries)
- [12. Create a GitHub PR](#12-create-a-github-pr)
- [13. Update your branch if needed.](#13-update-your-branch-if-needed)

### 1. Create a GitHub Account

Make sure you have a [GitHub account][github-join] and you are logged in with it.

### 2. Find an Issue to Work With

Visit the [brutils issues page][brutils-issues] and find an issue you would like to work with
and no one assigned to it yet.

Send a comment in the issue asking to work with it. Something like: "hey, can I work on this?".

Wait until someone assign you to the ticket. Once you are assigned to it, you can move to the next
step.

Please, feel free to ask any questions in the issue's page before or during the development
process.

When starting to contribute to the project, it is advisable to pick one issue at a time. This helps ensure that others also have the opportunity to collaborate and prevents resources from staying inactive for too long.

### 3. Install Git

Make sure you have [Git installed][install-git].

### 4. Fork the Project

[Fork the brutils repository][github-forking].

### 5. Clone your Fork

[Clone][github-cloning] your fork locally.

### 6. Create a New Branch

Go into the brutils folder:

```bash
$ cd brutils-python
```

And create a new branch:

```bash
$ git checkout -b <issue_number>
```

### 7. Run brutils locally
## Installation
### Requirements

- [Python 3.7+][python]
- [Poetry][poetry]

Create a [virtualenv][virtualenv] for brutils and activate it:

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

Now, you can use it [in the same way described in the README.md file](/README_EN.md#usage).

## Tests

```shell
$ make test
```

### 8. Make your changes

Now is the step where you can implement your changes in the code.

It is important to notice that we document our code using [docstrings][docstring-definition].
Modules, classes, functions, and methods should be documented. Your changes should also be well
documented and should reflect updated docstrings if any of the params were changed for a
class/attributes or even functions.

We follow the given pattern below to keep consistency in the docstrings:

```python
class Example:
    """Explain the purpose of the class

    Attributes:
        x[dict]: Short explanation here
        y[type, optional]: Short explanation here

    """

    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def foobar(self, w):
        """Purpose if the function

        Args:
            w[str]: Short explanation here

        Returns:
            value[str]: Short explanation here

        """
        ...
        return value

```

One last thing to keep in mind while self-documenting code with docstrings that you can ignore
docstrings in property decorators and magic methods.

### 9. Test your changes

#### Write new tests

Make sure you have created the necessary tests for every new change you made.

#### Make sure all tests passed

Run all the tests with `make test` and make sure that they all passed.

**PRs will not be merged if there is any test missing or failing.**

### 10. Commit and push your changes

Commit the changes:

```bash
$ git commit -a -m "<commit_message>"
```

Push your commit to GitHub:

```bash
$ git push --set-upstream origin <issue_number>
```

Create the number of changes/commits you need and push them.

### 11. Add changelog entries

[Add a changelog entry][keep-a-changelog] to CHANGELOG.md.

### 12. Create a GitHub PR

[Create a GitHub PR][github-creating-a-pr].

### 13. Update your branch if needed.

[Make sure your branch is updated with main][github-sync-pr].

# Release a New Version

Here you will find how to deploy a new production version of brutils:

- [1. Create a Release PR](#1-create-a-release-pr)
- [2. Deploy via GitHub](#2-deploy-via-github)

### 1. Create a Release PR

#### Bump the lib Version

Increment the version number, following the [Semantic Versioning][semantic-versioning],
in the `pyproject.toml` file: https://github.com/brazilian-utils/brutils-python/blob/main/pyproject.toml#L3

#### Update the CHANGELOG.md

Add a new version title with the new version number and the current date, like
[this](https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md?plain=1#L9).

And add the version links, like [this](https://github.com/brazilian-utils/brutils-python/blob/bc10b7242bd939cc445070f7e937e3ad187ff95a/CHANGELOG.md?plain=1#L33-L34)

#### Create the PR

Create a PR named `Release v<version>` containing these two changes above.

[Example of Release PR](https://github.com/brazilian-utils/brutils-python/pull/128)

#### Merge the PR

Once the PR has been accepted and passed on all checks, merge it.

### 2. Deploy via GitHub

Deploy production is automatically done when a [new release is created][creating-releases] on GitHub.

- The `tag version` should be `v<version>` (e.g `v2.0.0`).
- The `release title` should be the same as tag version (e.g `v2.0.0`).
- The `release description` should be the content copied from the CHANGELOG.md file from the
corresponding version section.

Real examples are available at: https://github.com/brazilian-utils/brutils-python/releases

When the Deploy on GitHub is done, the new version will be also automatically deployed on
[PyPI][brutils-on-pypi]. Download the new brutils version from PyPI and test if everything is
working as expected.


[brutils-issues]: https://github.com/brazilian-utils/brutils-python/issues
[brutils-on-pypi]: https://pypi.org/project/brutils/
[creating-releases]: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
[docstring-definition]: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
[github-cloning]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
[github-creating-a-pr]: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[github-forking]: https://docs.github.com/en/get-started/quickstart/contributing-to-projects
[github-join]: https://github.com/join
[github-sync-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
[install-git]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[keep-a-changelog]: https://keepachangelog.com/en/1.1.0/
[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[semantic-versioning]: https://semver.org/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
