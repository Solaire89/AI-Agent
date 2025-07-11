import os

def get_files_info(working_directory, directory=None):
    absolute_working_directory = os.path.abspath(working_directory) # Getting the absolute path of the working_directory
    absolute_directory = os.path.abspath(directory) # Getting the absolute path of the directory
    if not absolute_directory.startswith(absolute_working_directory): # CHecking if the absolute directory doesn't start with the absolute working directory
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' # Return the error message if it doesn't
    if not os.path.isdir(absolute_directory): # Checking if the directory isn't a directory
        return f'Error: {directory} is not a directory' # Returning the error message
    if directory is None: # Checking if the directory is None
        directory = "." # If it is, setting the directory to '.'
    full_directory = os.path.join(absolute_working_directory, directory) # Concatenating the working directory and directory to get the full absolute value
    item_names = os.listdir(full_directory) # Create a list of files/directories in the current directory
    item_list = [] # Creating a list of directory items to append the objects to in the following for loop
    for item in item_names:
        if os.path.isdir(item): 
            full_path = os.path.join(absolute_working_directory, item)
            item_list.append(f"{item}: file size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}")
    return "/n".join(item_list)