#!/bin/bash

echo "Checking and setting up the environment for GPU..."
source ~/miniconda3/bin/activate tf_gpu

echo "Launching Sort with Precision on GPU..."
python sort-with-precision.py