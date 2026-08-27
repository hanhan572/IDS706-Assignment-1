# IDS706 Assignment 1

This project is a simple Python application for IDS 706. It asks the user for a name and prints a welcome message for the Data Engineering course.

## Project Structure

* `src/main.py` — contains the `welcome_message` function and the main program
* `tests/test_main.py` — contains the unit test for `welcome_message`
* `requirements.txt` — lists the Python dependencies
* `Makefile` — provides commands for installation, testing, running, and Docker
* `Dockerfile` — builds the application in a Docker container
* `.github/workflows/test.yml` — runs automated tests with GitHub Actions

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

A successful test shot all tests passed.

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

This repository uses GitHub Actions to automatically install dependencies, run the Python tests, build the Docker image, and run the tests inside Docker whenever code is pushed to the repository.

## Repository

GitHub repository: `https://github.com/hanhan572/IDS706-Assignment-1`

## Author

Evelyn
