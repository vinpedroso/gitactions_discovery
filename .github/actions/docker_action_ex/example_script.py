import os

def main() -> None:
    input_var = int(os.environ["INPUT_LENGTH"])
    result_list = [i for i in range (1,input_var+1)]
    print(f"::set-output name=result::{result_list}")
    return None

if __name__ == "__main__":
    main()