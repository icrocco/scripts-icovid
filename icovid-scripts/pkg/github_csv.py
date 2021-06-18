import requests
import os

def github(url: str):
    token = os.environ.get("GITHUB_DATAGOV_TOKEN")
    try:
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3.raw"}
        return requests.get(url, headers=headers)

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)