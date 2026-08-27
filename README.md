# IDS706 Assignment 1

This project is a simple Python application for IDS 706. It asks the user for a name and prints a welcome message for the Data Engineering course.

The project also includes automated testing, Docker support, GitHub Actions, code formatting, linting, and a small bonus extension for improved input handling.

## Project Structure

* `src/main.py` — contains the `welcome_message` function, the bonus `personalized_welcome` function, and the main program
* `tests/test_main.py` — contains the original unit test and additional tests for the bonus functionality
* `requirements.txt` — lists the Python dependencies, including `pytest`, `black`, and `ruff`
* `Makefile` — provides commands for installation, testing, running, formatting, linting, Docker, and cleanup
* `Dockerfile` — builds the application in a Docker container
* `.dockerignore` — excludes unnecessary local files from the Docker build context
* `.github/workflows/test.yml` — runs automated checks with GitHub Actions
* `.gitignore` — prevents local files such as `.venv/` and cache files from being committed

## Setup

On macOS, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
make install
```

or:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

Run the program with:

```bash
make run
```

or:

```bash
python src/main.py
```

When prompted, enter your name:

```text
Enter your name: Evelyn
```

Example output:

```text
Evelyn, welcome to the Data Engineering course.
```

## Run Tests

Run the test suite with:

```bash
make test
```

or:

```bash
python -m pytest
```

A successful test run should show that all tests passed.

## Format and Lint

This project uses Black for code formatting and Ruff for linting.

Format the source code and tests:

```bash
make format
```

Run the linter:

```bash
make lint
```

These commands are also checked through GitHub Actions.

## Docker

Build the Docker image:

```bash
make docker-build
```

Run the tests inside Docker:

```bash
make docker-test
```

Run the application inside Docker:

```bash
make docker-run
```

## GitHub Actions

This repository uses GitHub Actions to automatically:

* install dependencies
* check code formatting with Black
* run linting with Ruff
* run the Python test suite
* build the Docker image
* run the tests inside Docker

The workflow runs whenever code is pushed to the repository or a pull request is created.

## Bonus Exploration

For the optional bonus exploration, I added a related `personalized_welcome` function.

This function improves input handling by:

* removing extra spaces around the user's name
* handling empty input without producing an awkward welcome message
* reusing the original `welcome_message` function when a valid name is provided

I also added additional unit tests to verify both whitespace handling and empty-name behavior while keeping the original required test unchanged.

For the Makefile extra credit, I added working `make format` and `make lint` targets using Black and Ruff. These checks are also included in the GitHub Actions workflow.

## Repository

GitHub repository: `https://github.com/hanhan572/IDS706-Assignment-1`

## Author

Evelyn Wang
