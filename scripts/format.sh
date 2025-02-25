#!/usr/bin/env bash
# format.sh

set -e

echo "Running black to format all Python files..."

pip install black
black --check src/ tests/

echo "Black formatting done!"
