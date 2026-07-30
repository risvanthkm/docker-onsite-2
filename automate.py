import requests

users=100

for user_id in range(users):
    url = "http://127.0.0.1:80"

    custom_headers = {
        "X-User-ID": str(user_id)
    }

    response = requests.get(url, headers=custom_headers)

