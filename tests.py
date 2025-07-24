from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file 

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for current file:")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for current file:")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for current file:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py")
    print("Result for current file:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for current file:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for current file:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for current file:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for current file:")
    print(result)
    print("")



if __name__ == "__main__":
    test()