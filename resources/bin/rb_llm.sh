#!/bin/bash

# Script that execute the LLM Llamafile to generate a title of given policies. 
# 
# Execution:
#     $ rb_llm.sh --options

# Verify if there are params
if [ "$#" -eq 0 ]; then
  echo "Error: No arguments provided."
  echo -e "Usage: ./rb_llm.sh --options...\nExecutes the LLM model.\nThe model used is Llamafile"
  exit 1
fi

# Verify the model exists
MODEL_PATH=/usr/lib/redborder/bin/llm-model

while [ ! -f "$MODEL_PATH" ]; do
  echo "Model not found at $MODEL_PATH. Retrying in 30 seconds..."
  sleep 30
done

echo "......Model found......"

/bin/bash "$MODEL_PATH" "$@"