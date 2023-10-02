#!/bin/bash/python3

# Check if the PYFILE environment variable is set
if [ -z "$PYFILE" ]; then
  echo "Error: PYFILE environment variable is not set."
  exit 1
fi

# Check if the specified Python script exists
if [ ! -f "$PYFILE" ]; then
  echo "Error: Python script '$PYFILE' not found."
  exit 1
fi

# Run the Python script
python3 "$PYFILE"

