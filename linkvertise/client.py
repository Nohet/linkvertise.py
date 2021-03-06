from typing import Union

from base64 import b64encode
from random import random

from urllib.parse import quote


class LinkvertiseClient:
    def __init__(self, **kwargs):
        self.linkvertise_url = kwargs.get("base_url") or "https://link-to.net"

    def btoa(self, _link: str):
        link_bytes = _link.encode("ascii")

        base64_bytes = b64encode(link_bytes)
        base64_link = base64_bytes.decode("ascii")

        return base64_link

    def linkvertise(self, user_id: Union[int, str], _link: str):
        base_url = f"{self.linkvertise_url}/{user_id}/{random() * 1000}/dynamic"
        href = base_url + "?r=" + str(self.btoa(quote(_link, safe="~@#$&()*!+=:;,.?/\'")))

        return href
