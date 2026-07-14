from functions.run_python_file import run_python_file


def main():
    print("main.py:")
    print(run_python_file("calculator", "main.py"))

    print("\nmain.py with argument:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\ntests.py:")
    print(run_python_file("calculator", "tests.py"))

    print("\noutside directory:")
    print(run_python_file("calculator", "../main.py"))

    print("\nnonexistent:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nnot python file:")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
