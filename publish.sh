#!/bin/bash

set -e
set -x

python setup.py check
python setup.py bdist_wheel
python setup.py register bdist_wheel upload -r pypi
