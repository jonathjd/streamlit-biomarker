import json
import requests


def load_lottie_file(path: str):
    with open(path, "r") as f:
        return json.load()


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()