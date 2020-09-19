#!/bin/bash
for py_file in $(find emulator_examples -name '*.py' -execdir basename {} .py ';')
do
    python -m emulator_examples.$py_file
done
