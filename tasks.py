#!/usr/bin/env python3
import os

from invoke import task


@task
def lint(c):
    """Pull Github's Superlinter image and run it against the current project."""
    # Pull latest Superlinter image from repo.
    c.run("docker pull github/super-linter:latest")
    current_wd = os.getcwd()
    c.run(f"docker run -e RUN_LOCAL=true -v {current_wd}:/tmp/lint github/super-linter")


@task
def build(c, image="base"):
    """Build the given Docker image."""
    c.run(f"docker build -t {image}-image")


@task
def test(c):
    """Run the test suite."""
    build(c, "test")
    c.run("docker run -t test-image")
