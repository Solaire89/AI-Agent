import os
from google.genai import types # type: ignore

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes in the python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Write to the file specified.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content used to write the file."
            ),
        },
        required=["file_path", "content"]
    ),
)