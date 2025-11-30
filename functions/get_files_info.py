import os
from google.genai import types # type: ignore

def get_files_info(working_directory, directory=None):
    absolute_working_directory = os.path.abspath(working_directory) 
    target_directory = absolute_working_directory
    if directory:
        target_directory = os.path.abspath(os.path.join(working_directory, directory))
    if not target_directory.startswith(absolute_working_directory): 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' 
    if not os.path.isdir(target_directory):
        return f'Error: {directory} is not a directory' 
    try:
        files_info = [] 
        for filename in os.listdir(target_directory):
            full_path = os.path.join(target_directory, filename)
            files_info.append(
                f"- {filename}: file size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}"
                )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info
    ]
)