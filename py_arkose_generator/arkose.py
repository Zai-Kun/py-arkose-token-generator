import random

from . import util


def get_values_for_request(options):
    """
    The get_values_for_request function is used to construct the data that will be sent in a request.
        It takes an options dictionary as input, and returns a dictionary containing the url, headers, and data for the request.
        The options dictionary can contain any of these keys:
            'data': A dict containing key-value pairs that will be sent with the request (e.g., {'text': 'Hello world!'})
            'pkey': The public key for your OpenAI API account (e.g., &quot;3D86FBBA-9D22-402A-B512-3420086BA

    Args:
        options: Pass in the data, pkey, surl and headers

    Returns:
        A dictionary with the following keys: url, header and data
    """

    options = {
        "data": {},
        "pkey": "3D86FBBA-9D22-402A-B512-3420086BA6CC",
        "surl": "https://tcr9i.chat.openai.com",
        "headers": {"User-Agent": util.DEFAULT_USER_AGENT},
        "site": "https://chat.openai.com",
        **options,
    }

    if "headers" not in options:
        options["headers"] = {"User-Agent": util.DEFAULT_USER_AGENT}
    elif "User-Agent" not in options["headers"]:
        options["headers"]["User-Agent"] = util.DEFAULT_USER_AGENT

    options["headers"]["Accept-Language"] = "en-US,en;q=0.9"
    options["headers"]["Sec-Fetch-Site"] = "same-origin"
    options["headers"]["Accept"] = "*/*"
    options["headers"][
        "Content-Type"
    ] = "application/x-www-form-urlencoded; charset=UTF-8"
    options["headers"]["sec-fetch-mode"] = "cors"

    if "site" in options:
        options["headers"]["Origin"] = options["surl"]
        options["headers"][
            "Referer"
        ] = f"{options['surl']}/v2/{options['pkey']}/1.5.5/enforcement.fbfc14b0d793c6ef8359e0e4b4a91f67.html"

    ua = options["headers"].get("User-Agent")

    data = util.constructFormData(
        {
            "bda": util.getBda(ua, options),
            "public_key": options["pkey"],
            "site": options["site"] if "site" in options else None,
            "userbrowser": ua,
            "capi_version": "1.5.5",
            "capi_mode": "inline",
            "style_theme": "default",
            "rnd": str(random.random()),
            **{f"data[{k}]": v for k, v in options["data"].items()},
            "language": options.get("language", "en"),
        }
    )

    args = {
        "url": f"{options['surl']}/fc/gt2/public_key/{options['pkey']}",
        "headers": options["headers"],
        "data": data,
    }
    return args
