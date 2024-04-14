#!/bin/bash

echo "Checking and setting up the environment for CPU..."
source ~/miniconda3/bin/activate tf_cpu

echo "Launching Sort with Precision on CPU..."
python sort-with-precision.py