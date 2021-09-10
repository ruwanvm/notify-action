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
*HOME*: {os.environ['HOME']}\n
*GITHUB_JOB*: {os.environ['GITHUB_JOB']}\n
*GITHUB_SHA*: {os.environ['GITHUB_SHA']}\n
*GITHUB_REPOSITORY_OWNER*: {os.environ['GITHUB_REPOSITORY_OWNER']}\n
*GITHUB_RUN_ID*: {os.environ['GITHUB_RUN_ID']}\n
*GITHUB_RUN_NUMBER*: {os.environ['GITHUB_RUN_NUMBER']}\n
*GITHUB_RETENTION_DAYS*: {os.environ['GITHUB_RETENTION_DAYS']}\n
*GITHUB_ACTOR*: {os.environ['GITHUB_ACTOR']}\n
*GITHUB_WORKFLOW*: {os.environ['GITHUB_WORKFLOW']}\n
*GITHUB_HEAD_REF*: {os.environ['GITHUB_HEAD_REF']}\n
*GITHUB_BASE_REF*: {os.environ['GITHUB_BASE_REF']}\n
*GITHUB_EVENT_NAME*: {os.environ['GITHUB_EVENT_NAME']}\n
*GITHUB_SERVER_URL*: {os.environ['GITHUB_SERVER_URL']}\n
*GITHUB_API_URL*: {os.environ['GITHUB_API_URL']}\n
*GITHUB_GRAPHQL_URL*: {os.environ['GITHUB_GRAPHQL_URL']}\n
*GITHUB_WORKSPACE*: {os.environ['GITHUB_WORKSPACE']}\n
*GITHUB_ACTION*: {os.environ['GITHUB_ACTION']}\n
*GITHUB_EVENT_PATH*: {os.environ['GITHUB_EVENT_PATH']}\n
*GITHUB_ACTION_REPOSITORY*: {os.environ['GITHUB_ACTION_REPOSITORY']}\n
*GITHUB_ACTION_REF*: {os.environ['GITHUB_ACTION_REF']}\n
*GITHUB_PATH*: {os.environ['GITHUB_PATH']}\n
*GITHUB_ENV*: {os.environ['GITHUB_ENV']}\n
*RUNNER_OS*: {os.environ['RUNNER_OS']}\n
*RUNNER_TOOL_CACHE*: {os.environ['RUNNER_TOOL_CACHE']}\n
*RUNNER_TEMP*: {os.environ['RUNNER_TEMP']}\n
*RUNNER_WORKSPACE*: {os.environ['RUNNER_WORKSPACE']}\n
*ACTIONS_RUNTIME_URL*: {os.environ['ACTIONS_RUNTIME_URL']}\n
*ACTIONS_RUNTIME_TOKEN*: {os.environ['ACTIONS_RUNTIME_TOKEN']}\n
*ACTIONS_CACHE_URL*: {os.environ['ACTIONS_CACHE_URL']}
        """
    }
    response = requests.post(webhook, data=json.dumps(encoded_message), headers={'Content-Type': 'application/json'})

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
