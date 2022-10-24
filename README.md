python3 -m venv .venv
source .venv/bin/activate
pip install flask pytest
pip freeze > requirements.txt
export PYTHONPATH=src
echo $PYTHONPATH
deactivate
source .venv/bin/activate
enter command "pytest" from root
