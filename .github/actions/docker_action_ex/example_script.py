import os

def main() -> None:
    input_var = int(os.environ["INPUT_LENGTH"])
    result_number = input_var - 5
    print(f'result="{result_number}" >> $GITHUB_OUTPUT')
    return None

if __name__ == "__main__":
    main()