import os

def main() -> None:
    input_var = int(os.environ["INPUT_INIT-NUMBER"])
    result_number = input_var - 5
    bash_cmd = f'echo "final-number={result_number}" >> $GITHUB_OUTPUT'
    os.system(bash_cmd)
    return None

if __name__ == "__main__":
    main()