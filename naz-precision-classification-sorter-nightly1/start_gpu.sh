#!/bin/bash
echo "Checking and setting up the environment for GPU..."
source activate tf_gpu

echo "Launching Sort with Precision on GPU..."
python sort-with-precision.py
read -p "Press any key to continue..."