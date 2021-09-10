import os


def main():
    webhook = os.environ['INPUT_WEBHOOK']
    message = os.environ['INPUT_MESSAGE']

    results = f"{message} is send to {webhook}"

    # Add notify code here

    print(f"::set-output name=results::{results}")


if __name__ == "__main":
    main()
