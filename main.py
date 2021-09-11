import os
import requests
import json


def main():
    webhook = os.environ["INPUT_WEBHOOK"]
    message = os.environ['INPUT_MESSAGE']
    git_repo = os.environ['GITHUB_REPOSITORY']
    repo_branch = os.environ['GITHUB_REF']

    encoded_message = dict(
        text=f"""*Repo* : {git_repo}\n*Branch* : {repo_branch}\n*Details* : {message}\n*User*: {os.environ['GITHUB_ACTOR']}\n*Event*: {os.environ['GITHUB_EVENT_NAME']}""")
    response = requests.post(webhook, data=json.dumps(encoded_message), headers={'Content-Type': 'application/json'})

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
