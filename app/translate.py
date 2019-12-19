import json
import urllib
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if (
        "YANDEX_TRANSLATOR_KEY" not in current_app.config
        or not current_app.config["YANDEX_TRANSLATOR_KEY"]
    ):
        return _("Error: the translation service is not configured.")
    API_ENDPOINT = "https://translate.yandex.net/api/v1.5/tr.json/translate?{}"
    API_KEY = current_app.config["YANDEX_TRANSLATOR_KEY"]
    params = urllib.parse.urlencode(
        {"lang": "{}-{}".format(source_language, dest_language), "key": API_KEY}
    )
    url = API_ENDPOINT.format(params)
    data = urllib.parse.urlencode({"text": text}).encode("utf8")

    r = urllib.request.urlopen(url, data)
    response = r.read()
    return json.loads(response.decode("utf-8-sig"))["text"][0]
