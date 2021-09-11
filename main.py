import os
import requests
import json


def main():
    webhook = os.environ["INPUT_WEBHOOK"]
    message = os.environ['INPUT_MESSAGE']
    git_repo = os.environ['GITHUB_REPOSITORY']
    repo_branch = os.environ['GITHUB_REF']

    encoded_message = {
        "text": {
            "contentType": "application/vnd.microsoft.card.receipt",
            "content": {
                "title": "John Doe",
                "facts": [
                    {
                        "key": "Order Number",
                        "value": "1234"
                    },
                    {
                        "key": "Payment Method",
                        "value": "VISA 5555-****"
                    }
                ],
                "items": [
                    {
                        "title": "Data Transfer",
                        "image": {
                            "url": "https://github.com/amido/azure-vector-icons/raw/master/renders/traffic-manager.png"
                        },
                        "price": "$ 38.45",
                        "quantity": "368"
                    },
                    {
                        "title": "App Service",
                        "image": {
                            "url": "https://github.com/amido/azure-vector-icons/raw/master/renders/cloud-service.png"
                        },
                        "price": "$ 45.00",
                        "quantity": "720"
                    }
                ],
                "total": "$ 90.95",
                "tax": "$ 7.50",
                "buttons": [
                    {
                        "type": "openUrl",
                        "title": "More information",
                        "image": "https://account.windowsazure.com/content/6.10.1.38-.8225.160809-1618/aux-pre/images/offer-icon-freetrial.png",
                        "value": "https://azure.microsoft.com/en-us/pricing/"
                    }
                ]
            }
        }
    }
    response = requests.post(webhook, data=json.dumps(encoded_message), headers={'Content-Type': 'application/json'})

    output = f"{message} is send with status {response.status_code}"

    print(f"::set-output name=results::{output}")


if __name__ == "__main__":
    main()
