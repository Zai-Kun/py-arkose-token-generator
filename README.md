# PY arkose-token generator

## Example usage

```python
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
response = requests.get(**args_for_request)
decoded_json = response.json()

if "token" in decoded_json:
    print(decoded_json["token"])
else:
    print(f"Error!\n {decoded_json}")

# Output: 454179210495214b7.0967231805|r=eu-west-1|meta=3|metabgclr=transparent|metaiconclr=%23757575|guitextcolor=%23000000|lang=en|pk=3D86FBBA-9D22-402A-B512-3420086BA6CC|at=40|sup=1|rid=16|ag=101|cdn_url=https%3A%2F%2Ftcr9i.chat.openai.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com|surl=https%3A%2F%2Ftcr9i.chat.openai.com|smurl=https%3A%2F%2Ftcr9i.chat.openai.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager

```

Originally translated from [funcaptcha](https://github.com/noahcoolboy/funcaptcha)
