.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: ghapi docs

ghapi: $(SRC)
	nbdev_build_lib
	touch ghapi

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	sleep 1
	fastrelease_conda_package --mambabuild --upload_user fastai
	nbdev_bump_version

conda_release:
	fastrelease_conda_package --mambabuild --upload_user fastai

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
