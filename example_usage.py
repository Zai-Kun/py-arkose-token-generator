import requests
from py_arkose_generator.arkose import get_values_for_request

opt = {
    "pkey": "3D86FBBA-9D22-402A-B512-3420086BA6CC",
    "surl": "https://tcr9i.chat.openai.com",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    },
    "site": "https://chat.openai.com",
}

args_for_request = get_values_for_request(opt)
response = requests.post(**args_for_request)
decoded_json = response.json()

if "token" in decoded_json:
    print(decoded_json["token"])
else:
    print(f"Error!\n {decoded_json}")
