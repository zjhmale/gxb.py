#!/bin/bash

set -e
set -x

for version in 2.7.3 3.4.6 3.5.3 3.6.1; do
    pyenv install $version
done

# https://github.com/pyenv/pyenv-virtualenv/issues/202
pyenv virtualenv -p python2.7 2.7.3 py27
pyenv virtualenv -p python3.4 3.4.6 py34
pyenv virtualenv -p python3.5 3.5.3 py35
pyenv virtualenv -p python3.6 3.6.1 py36

pip install -r requirements.txt
pip install -r test-requirements.txt

pyenv shell py36 py35 py34 py27 3.6.1

pytest -v tests
