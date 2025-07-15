from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for current directory:")
    print(result)
    print("")


if __name__ == "__main__":
    test()