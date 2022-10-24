1.python3 -m venv .venv
2.source .venv/bin/activate
3.pip install flask pytest
4.pip freeze > requirements.txt
5.export PYTHONPATH=src
6.echo $PYTHONPATH
7.deactivate
8.source .venv/bin/activate
9.enter command "pytest" from root
