#!/bin/bash

# Specify the path to your folder containing the images
image_folder="dataset/tablet_imgs/"

# Change to the image folder
cd "$image_folder"

# Loop through all the PNG files in the folder
for image in *.png; do
    # Extract relevant parts of the filename using pattern matching
    if [[ $image =~ ^(.+)_HeiCuBeDa_(.+)(_(back|front)\.png)$ ]]; then
        prefix="${BASH_REMATCH[1]}"
        suffix="${BASH_REMATCH[3]}"
        new_filename="${prefix}${suffix}"
 
        # Print the proposed name change
        echo "Proposed name change: $new_filename"
        mv "$image" "$new_filename"

    fi
done

echo "Name change preview complete. No files have been renamed."

