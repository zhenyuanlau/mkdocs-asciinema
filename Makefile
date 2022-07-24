Q := @

.PHONY: init deps build clean

deps:
	. $(VENV)/activate && pip freeze > requirements.txt

init:
	. $(VENV)/activate && pip install -r requirements.txt
build:
	. $(VENV)/activate && python -m build

clean:
	rm -fr dist *.egg-info


include Makefile.venv
