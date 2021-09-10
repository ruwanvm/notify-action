import os
import requests
import json


def main():
    webhook = os.environ["INPUT_WEBHOOK"]
    message = os.environ['INPUT_MESSAGE']
    git_repo = os.environ['GITHUB_REPOSITORY']
    repo_branch = os.environ['GITHUB_REF']

    encoded_message = {
        'text': f"""
        *Repo* : {git_repo}\n
        *Branch* : {repo_branch}\n
        *Details* : {message}\n
        {os.environ['HOME']}\n
        {os.environ['GITHUB_JOB']}\n
        {os.environ['GITHUB_SHA']}\n
        {os.environ['GITHUB_REPOSITORY_OWNER']}\n
        {os.environ['GITHUB_RUN_ID']}\n
        {os.environ['GITHUB_RUN_NUMBER']}\n
        {os.environ['GITHUB_RETENTION_DAYS']}\n
        {os.environ['GITHUB_ACTOR']}\n
        {os.environ['GITHUB_WORKFLOW']}\n
        {os.environ['GITHUB_HEAD_REF']}\n
        {os.environ['GITHUB_BASE_REF']}\n
        {os.environ['GITHUB_EVENT_NAME']}\n
        {os.environ['GITHUB_SERVER_URL']}\n
        {os.environ['GITHUB_API_URL']}\n
        {os.environ['GITHUB_GRAPHQL_URL']}\n
        {os.environ['GITHUB_WORKSPACE']}\n
        {os.environ['GITHUB_ACTION']}\n
        {os.environ['GITHUB_EVENT_PATH']}\n
        {os.environ['GITHUB_ACTION_REPOSITORY']}\n
        {os.environ['GITHUB_ACTION_REF']}\n
        {os.environ['GITHUB_PATH']}\n
        {os.environ['GITHUB_ENV']}\n
        {os.environ['RUNNER_OS']}\n
        {os.environ['RUNNER_TOOL_CACHE']}\n
        {os.environ['RUNNER_TEMP']}\n
        {os.environ['RUNNER_WORKSPACE']}\n
        {os.environ['ACTIONS_RUNTIME_URL']}\n
        {os.environ['ACTIONS_RUNTIME_TOKEN']}\n
        {os.environ['ACTIONS_CACHE_URL']}
        """
    }
    response = requests.post(webhook, data=json.dumps(encoded_message), headers={'Content-Type': 'application/json'})

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
