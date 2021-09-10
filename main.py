# import os
# import requests
# import json
#
#
# def main():
#     webhook = os.environ['INPUT_WEBHOOK']
#     message = os.environ['INPUT_MESSAGE']
#
#     results = f"{message} is send to {webhook}"
#
#     message = {'text': message}
#     response = requests.post(webhook, data=json.dumps(message), headers={'Content-Type': 'application/json'})
#
#     print(f"::set-output name=results::{results}")
#
#
# if __name__ == "__main":
#     main()

import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_WEBHOOK"]

    my_output = f"Hello {my_input}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
