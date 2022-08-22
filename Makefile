.PHONY: generate-docs test build
.SILENT: generate-docs test build

generate-docs:
	tox -e docs

test:
	tox --develop

build:
	tox --notest
