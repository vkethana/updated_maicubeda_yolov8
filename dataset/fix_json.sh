#!/bin/bash

# Specify the path to your folder containing the files
folder_path="annotations"

# Change to the folder
cd "$folder_path"
ls

# Loop through all the files with the "_03_" substring
for file in *_06_*.json; do
    # Extract the filename without the substring
    new_file="${file/_06_/_}"

    # Print the proposed name change
    echo "Proposed name change: $file -> $new_file"

    # Rename the file
    #mv "$file" "$new_file"
done

echo "Renaming complete."

