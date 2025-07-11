from functions.get_files_info import get_files_info

def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

if __name__ == "__main__":
    test()