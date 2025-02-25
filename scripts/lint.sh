#!/usr/bin/env bash

set -e

echo "Running pylint on all Python files..."

pip install pylint
pylint src/*.py tests/*.py --fail-under=8.0

echo "Pylint checks passed!"
