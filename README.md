# Goal
What is this project? Its aim is to provide a simple skeleton for a Python application with a full
development environment already available and a file structure pre-established. The goal is to have
sensible defaults and a minimum of powerful tool for task execution and automation. To achieve this
the project includes the following librairies.

## Docker
Docker is well-known accross the software engineering world. It allows developers to wrap their
applications and run them inside `dockers`, containers where the environment is standardized.
Developers build an image from a set of dependencies which will become immutable once the
application is running, allowing them to have a stable environment for production.

The current Docker images inside the `Dockerfile` are simple and use a multi-stage build pattern
to create a base image containing our application and a test image on top of it to allow our tests
to run.

## Invoke
Invoke is a library that allows us to create and execute tasks, just like a Makefile but in Python,
simplifying the whole ordeal.

## Pytest
Pytest is the de facto library to test applications in Python.

## Super-linter
Super-linter is a project developed by the Github team to provide developers with linters (syntax,
format and type checkers) for different languages. It integrates neatly with Github Actions for
CI/CD but in our case, we use it locally to run `flake8`, `pylint`, `black` and `isort`.

## Mypy
Mypy is a type checker for Python. While Python is weakly typed, the latest iteration, starting with
Python 3.5 have allowed us to ensure that our code works on another level by providing type hints.
While a lot of projects have to still to provide public type hints for their APIs, some already do
or have internal typing that we can query (Pytest for example.)








