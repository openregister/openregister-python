all:	flake8 test coverage

test:
	py.test -s

coverage:
	coverage run --source thingstance -m py.test && coverage report

coveralls:
	py.test --cov systemofrecord tests/ --cov-report=term --cov-report=html

flake8:
	flake8 thingstance tests

dist:
	python3 setup.py sdist

clean:
