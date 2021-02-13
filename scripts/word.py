from .translation import Translation

class Word:
    def __init__(self, _uuid, _name, _translations):
        self.uuid = _uuid
        self._name = _name
        self._translations = _translations
        
    def GetName(self): return self._name

    def GetTranslations(self): return self._translations

    def AddTranslation(self, _translation):
        self._translations.append(_translation)
    
    def RemoveTranslation(self, _translation):
        self._translations.remove(_translation)