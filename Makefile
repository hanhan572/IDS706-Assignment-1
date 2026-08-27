.PHONY: install test run docker-build docker-run docker-test clean format lint

IMAGE_NAME := data-engineering-demo

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest -q

run:
	python src/main.py

format:
	python -m black src tests

lint:
	python -m ruff check src tests

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run -it --rm $(IMAGE_NAME)

docker-test:
	docker run --rm $(IMAGE_NAME) python -m pytest -q

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .ruff_cache