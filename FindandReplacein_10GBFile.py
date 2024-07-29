import re
import os

def replace_in_large_file(file_path, chunk_size=1024*1024):
    pattern = re.compile(r"aaa")
    replace_with = "AAA"
    temp_file_path = file_path + '.tmp'

    with open(file_path, 'r') as input_file, open(temp_file_path, 'w') as temp_file:
        buffer = ''
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break

            buffer += chunk
            # Ensure that we don't cut off a match in the middle
            if len(buffer) > chunk_size:
                buffer_end = buffer[-len("aaa"):]
                buffer = buffer[:-len("aaa")]
            else:
                buffer_end = ''

            buffer = pattern.sub(replace_with, buffer)
            temp_file.write(buffer)
            buffer = buffer_end

        # Process the remaining buffer
        if buffer:
            buffer = pattern.sub(replace_with, buffer)
            temp_file.write(buffer)

    # Replace the original file with the modified temporary file
    os.replace(temp_file_path, file_path)

# Example usage
file_path = 'large_file.txt'
replace_in_large_file(file_path)
