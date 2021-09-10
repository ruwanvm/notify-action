import os


def main():
    webhook = os.environ['INPUT_WEBHOOK']
    message = os.environ['message']

    results = f"{message} is send to {webhook}"

    print(f"::set-output name=results::{results}")


if __name__ == "__main":
    main()
