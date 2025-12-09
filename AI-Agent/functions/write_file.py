import os

def write_file(working_directory, file_path, content):
    absolute_working_directory = os.path.abspath(working_directory)
    # Join the working directory and file path
    absolute_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        parent_directory = os.path.dirname(absolute_file_path)
        os.makedirs(parent_directory, exist_ok=True)
        with open(absolute_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'