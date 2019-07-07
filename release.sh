#!/bin/bash
rm -rf build && rm -rf dist && rm -rf scv.egg* && rm -rf *.egg-info
# echo -e "Is the version number upgraded? (y/n)"
# python setup.py sdist bdist_wheel
# twine upload dist/
#
# twine upload -r local --sign -identity user_name ./foo-1.zip
# twine upload --repository-url https://pypi.misaka.ink/ dist/*