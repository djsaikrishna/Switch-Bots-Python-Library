import swibots
from swibots.base import SwitchObject


class CallbackResponse(SwitchObject):
    def __init__(self, app: "swibots.App" = None, **kwargs):
        super().__init__(app, **kwargs)
    
    @property
    def type(self) -> str:
        return "answerCallback"
