import os
import requests
import json


def main():
    webhook = os.environ["INPUT_WEBHOOK"]
    message = os.environ['INPUT_MESSAGE']
    status = os.environ['INPUT_STATUS']
    git_repo = os.environ['GITHUB_REPOSITORY']
    repo_branch = os.environ['GITHUB_REF']
    user = os.environ['GITHUB_ACTOR']
    job = os.environ['GITHUB_JOB']
    run_no = os.environ['GITHUB_RUN_NUMBER']

    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": git_repo
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"On {repo_branch} - {job} ({run_no})"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*User*: {user}"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Status*: {status}"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "*Message* : Test Message from Another repo"
                    }
                ]
            }
        ]
    }

    response = requests.post(webhook, data=json.dumps(payload), headers=headers)

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
