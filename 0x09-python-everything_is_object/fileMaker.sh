#!/bin/bash


if [ $# -ne 2 ]; then
  echo "Usage: $0 <filename> <count>"
  exit 1
fi

filename="$1"
count="$2"


if ! [[ "$count" =~ ^[0-9]+$ ]] || [ "$count" -lt 0 ]; then
  echo "Count must be a non-negative integer."
  exit 1
fi

# Create files with enumerated names
for ((i = 0; i <= count; i++)); do
  new_filename="${i}-${filename}"
  touch "$new_filename"
  echo "Created file: $new_filename"
done

echo "Files created successfully."
echo "Have A Good Day Friend A.M"
