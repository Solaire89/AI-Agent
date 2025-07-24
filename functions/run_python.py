import subprocess
import os

def run_python_file(working_directory, file_path, args=[]):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))
    if not absolute_file_path.startswith(absolute_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(
            ['python', absolute_file_path, *args], 
            capture_output=True, 
            text=True, 
            cwd=absolute_working_directory, 
            timeout=30
        )
        if result.returncode != 0:
            output += f"\nProcess exited with code {result.returncode}"
        if not result.stderr and not result.stdout:
            return 'No output produced.'
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"