PYTHON=python3

src_name = ./app
test_name = ./app/tests


.PHONY: build
build:
	docker-compose -f docker-compose.yml -f docker-compose-build.yml build

.PHONY: remove
remove:
	docker container prune
	rm -rf ./mongo/data/*

.PHONY: format
format: 
	black --line-length 88 $(src_name)

.PHONY: flake
flake: 
	flake8 $(src_name) \
		--max-line-length=88

.PHONY: lint
lint: 
	pylint $(src_name)\
		--disable=missing-docstring \
		--disable=fixme \
		--disable=no-else-return \
		--ignored-argument-names=[args,kwargs]

.PHONY: type
type: 
	mypy $(src_name)

.PHONY: test
test: 
	pytest $(test_name) -s --disable-pytest-warnings

.PHONY: checklist
checklist: format flake test

.PHONY: clean
clean:
	find . -type f -name "*.pyt" | xargs rm -rf
	find . -type d -name __pycache__ | xargs rm -rf
