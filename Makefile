PYTHON=python3

src_dir = ./GraphQL


.PHONY: app
app:
	docker-compose -f docker-compose.yml -f docker-compose-build.yml up

.PHONY: ci
ci:
	docker-compose -f docker-compose-ci.yml up

.PHONY: format
format: 
	black --line-length 88 $(src_dir)

.PHONY: flake
flake: 
	flake8 $(src_dir) \
		--max-line-length=88

.PHONY: lint
lint: 
	pylint $(src_dir)\
		--disable=missing-docstring \
		--disable=fixme \
		--disable=no-else-return \
		--ignored-argument-names=[args,kwargs]

.PHONY: type
type: 
	mypy $(src_dir)

.PHONY: checklist
checklist: format flake

.PHONY: clean
clean:
	find . -type f -name "*.pyt" | xargs rm -rf
	find . -type d -name __pycache__ | xargs rm -rf
