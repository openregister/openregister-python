all:	flake8 test coverage

test:
	py.test -s

coverage:
	coverage run --source thingstance -m py.test && coverage report

flake8:
	flake8 thingstance tests

dist:
	python3 setup.py sdist

clean:
