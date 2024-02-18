import os

def main() -> None:
    input_var = int(os.environ["INPUT_INIT-NUMBER"])
    result_number = input_var - 5
    print(f'::set-output name=final-number::{result_number}')
    return None

if __name__ == "__main__":
    main()