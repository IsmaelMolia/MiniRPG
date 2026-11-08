MAIN = src/main.py
REQUIREMENTS = requirements.txt
PYTHON = python3
VENVPATH = ./.venv


all: run


run: dependencies
	$(VENVPATH)/bin/python $(MAIN)


dependencies: $(VENVPATH)
	$(VENVPATH)/bin/pip install -r $(REQUIREMENTS)


$(VENVPATH):
	$(PYTHON) -m venv $(VENVPATH)


clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +


fclean: clean
	rm -rf $(VENVPATH)


re: fclean run


.PHONY: all run dependencies clean fclean re
