# SUM
## Setup environment
git clone git@github.com:Teams21/SUM.git
cd SUM
python -m venv .
python -m pip install -U pip
pip install -r requirements.txt

## Setup development
git checkout -b branch_name
do work...
first push:
git push -u origin branch_name
all other push commands:
git push

merge when done (use pull requests)