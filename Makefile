.PHONY: all test coverage coveralls flake8 dist clean

all:	flake8 test coverage

test:
	py.test -v -s

coverage:
	coverage run --source openregister -m py.test && coverage report

coveralls:
	py.test --cov openregister tests/ --cov-report=term --cov-report=html

flake8:
	flake8 openregister tests

dist:
	python3 setup.py sdist upload

init:
	pip3 install -r requirements/production.txt
	pip3 install -r requirements/test.txt

clean:
	-find . -name "*.pyc" | xargs rm -f
	-find . -name "__pycache__" | xargs rm -rf
	-rm -rf dist
	-rm -rf build
	-rm -rf openregister_openregister.egg-info
