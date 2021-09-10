import os
import requests
import json


def main():
    webhook = os.environ['INPUT_WEBHOOK']
    message = os.environ['INPUT_MESSAGE']

    results = f"{message} is send to {webhook}"

    message = {'text': message}
    response = requests.post(webhook, data=json.dumps(message), headers={'Content-Type': 'application/json'})

    results = response.status_code

    print(f"::set-output name=results::{results}")


if __name__ == "__main":
    main()
