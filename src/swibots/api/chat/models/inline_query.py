from typing import List, Optional
import swibots
from swibots.base import SwitchObject

from swibots.utils.types import JSONDict


class InlineQuery(SwitchObject):
    def __init__(
        self,
        app: "swibots.App" = None,
        text: Optional[str] = None,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
    ):
        super().__init__(app)
        self.text = text
        self.url = url
        self.callback_data = callback_data

    def to_json(self) -> JSONDict:
        return {
            "text": self.text,
            "url": self.url,
            "callbackData": self.callback_data,
        }

    def from_json(self, data: JSONDict) -> "InlineQuery":
        if data is not None:
            self.text = (data.get("text"),)
            self.url = (data.get("url"),)
            self.callback_data = (data.get("callbackData"),)
        return self
