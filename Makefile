.PHONY: all test coverage coveralls flake8 dist clean

all:	flake8 test coverage

test:
	py.test -s

coverage:
	coverage run --source thingstance -m py.test && coverage report

coveralls:
	py.test --cov thingstance tests/ --cov-report=term --cov-report=html

flake8:
	flake8 thingstance tests

dist:
	python3 setup.py sdist upload

clean:
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	-rm -rf dist
	-rm -rf build
	-rm -rf tiddlyweb.egg-info
