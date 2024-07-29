import re

def replace_in_file(input_file_path, output_file_path, search_pattern, replace_string):
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        buffer_size = 8 * 1024 * 1024  # 8 MB buffer size
        buffer = infile.read(buffer_size)

        while buffer:
            # Use re.sub() for pattern-based replacement
            modified_buffer = re.sub(search_pattern, replace_string, buffer)
            outfile.write(modified_buffer)
            buffer = infile.read(buffer_size)

if __name__ == "__main__":
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    search_pattern = r'find_me'  # Example regex pattern
    replace_string = 'replace_with'

    replace_in_file(input_file_path, output_file_path, search_pattern, replace_string)
