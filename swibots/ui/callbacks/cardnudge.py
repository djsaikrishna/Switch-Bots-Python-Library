import swibots
from swibots.base import SwitchObject
from .callbackresponse import CallbackResponse


class CardNudge(CallbackResponse):
    def __init__(self, app: "swibots.App" = None, **kwargs):
        super().__init__(app, **kwargs)

    @property
    def type(self) -> str:
        return "card_nudge"

    def to_json(self, data: dict=None) -> "CardNudge":
        pass