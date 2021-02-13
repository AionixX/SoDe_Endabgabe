from .translation import Translation

class NullTranslation(Translation):
    def __init__(self):
        self._uuid = ""
        self.text = "(Keine)"