#!/bin/bash

# Directory containing the files
directory=$1

# Check if the "thumb" folder exists, create it if not
thumb_dir="${directory}/thumb"
if [ ! -d "$thumb_dir" ]; then
    mkdir "$thumb_dir"
fi

# Maximum file size in kilobytes (e.g., 100KB)
max_file_size=500

# Loop through each JPG file in the directory
for file in "${directory}"/*.jpg; do
    if [ -f "$file" ]; then
        # Extract the filename from the path
        filename=$(basename "$file")

        # Check if the file is not already in the "thumb" folder
        if [ ! -f "${thumb_dir}/${filename}" ]; then
            # Set an initial width
            width=1000

            # Create the initial thumbnail
            convert "$file" -auto-orient -thumbnail "${width}x" -unsharp 0x.5 "${thumb_dir}/${filename}"

            # Calculate the initial file size
            file_size=$(du -k "${thumb_dir}/${filename}" | awk '{print $1}')

            # Continuously reduce the width until the file size is below the threshold
            while [ "$file_size" -gt "$max_file_size" ] && [ "$width" -gt 100 ]; do
                width=$((width - 100))
                convert "$file" -auto-orient -thumbnail "${width}x" -unsharp 0x.5 "${thumb_dir}/${filename}"
                file_size=$(du -k "${thumb_dir}/${filename}" | awk '{print $1}')
            done
        fi
    fi
done

