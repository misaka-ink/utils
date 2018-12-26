#!/bin/bash
rm -rf build && rm -rf dist && rm -rf scv.egg* && rm -rf *.egg-info
# echo -e "Is the version number upgraded? (y/n)"
# python setup.py sdist bdist_wheel
# twine upload dist/*