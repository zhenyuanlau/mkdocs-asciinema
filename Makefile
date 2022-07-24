Q := @

.PHONY: init deps build testpypi pypi clean

deps:
	. $(VENV)/activate && pip freeze > requirements.txt

init:
	. $(VENV)/activate && pip install -r requirements.txt
build:
	. $(VENV)/activate && python -m build
testpypi:
	. $(VENV)/activate && python -m twine upload -r testpypi dist/*

pypi:
	. $(VENV)/activate && python -m twine upload dist/*

clean:
	rm -fr dist

include Makefile.venv
