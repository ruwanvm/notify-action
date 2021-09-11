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
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": git_repo,
        "sections": [{
            "activityTitle": git_repo,
            "activitySubtitle": f"On {repo_branch} - {job} ({run_no})",
            "activityImage": "https://teamsnodesample.azurewebsites.net/static/img/image6.png",
            "facts": [{
                "name": "User",
                "value": user
            }, {
                "name": "Status",
                "value": status
            }, {
                "name": "Message",
                "value": message
            }],
            "markdown": True
        }]
    }

    response = requests.post(webhook, data=json.dumps(payload), headers=headers)

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
