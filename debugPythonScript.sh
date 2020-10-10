#!/bin/bash

if [ "$1" != "" ]; then
    python3 -m pdb $1
else
    echo "Indicare lo script in python di cui fare debug."
fi
