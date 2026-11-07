import sys
import pycomo


def main():
    print("Environment Check")
    print("-----------------")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"PyCoMo location: {pycomo.__file__}")
    print("Environment is ready!")


if __name__ == "__main__":
    main()