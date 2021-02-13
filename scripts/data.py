adminPath = 'jsonData/Admin.json'
translatorPath = 'jsonData/Translator.json'
userPath = 'jsonData/User.json'
wordsPath = 'jsonData/Words.json'
languagesPath = 'jsonData/Languages.json'


class Data():
    class _Data():
        def __init__(self):
            self.LoadData()
            self.activeUser = self.user

        def LoadData(self):
            with open(wordsPath) as words_json:
                self.words = self.CreateWords(json.load(words_json))

            with open(languagesPath) as language_json:
                self.languages = self.CreateLanguages(json.load(language_json))

            with open(userPath) as user_json:
                self.user = self.CreateUser(json.load(user_json))

            with open(translatorPath) as translator_json:
                self.translator = self.CreateTranslator(json.load(translator_json))

            with open(adminPath) as admin_json:
                self.admin = self.CreateAdmin(json.load(admin_json))

        def CreateWords(self, _data):
            words = []
            for word in _data:
                uuid = word['uuid']
                name = word['name']
                translations = self.CreateTranslations(word['translations'])
                words.append(Word(uuid, name, translations))
            
            return words

        def CreateTranslations(self, _data):
            translations = []
            for translation in _data:
                uuid = translation['uuid']
                text = translation['text']
                language = translation['language']
                translations.append(Translation(uuid, text, language))
            
            return translations

        def CreateLanguages(self, _data):
            languages = []
            for language in _data:
                uuid = language['uuid']
                name = language['name']
                languages.append(Language(uuid, name))

            return languages

        def CreateUser(self, _data):
            createdWords = _data['createdWords']
            return User(createdWords)

        def CreateTranslator(self, _data):
            createdWords = _data['createdWords']
            name = _data['name']
            password = _data['password']
            translationRights = _data['translationRights']
            translatedWords = _data['translatedWords']
            return Translator(createdWords, name, password, translationRights, translatedWords)

        def CreateAdmin(self, _data):
            createdWords = _data['createdWords']
            name = _data['name']
            password = _data['password']
            translationRights = _data['translationRights']
            translatedWords = _data['translatedWords']
            return Admin(createdWords, name, password, translationRights, translatedWords)

        def SaveData(self):
            self.SaveWords()
            self.SaveLanguages()
            self.SaveUser()
            self.SaveTranslator()
            self.SaveAdmin()

        def SaveWords(self):
            wordsFile = open(wordsPath, 'w')
            wordsFile.write(json.dumps(self.words, indent=4, cls=Encoder))
            wordsFile.close()

        def SaveLanguages(self):
            languageFile = open(languagesPath, 'w')
            languageFile.write(json.dumps(self.languages, indent=4, cls=Encoder))
            languageFile.close()
        
        def SaveUser(self):
            userFile = open(userPath, 'w')
            userFile.write(json.dumps(self.user, indent=4, cls=Encoder))
            userFile.close()

        def SaveTranslator(self):
            translatorFile = open(translatorPath, 'w')
            translatorFile.write(json.dumps(self.translator, indent=4, cls=Encoder))
            translatorFile.close()

        def SaveAdmin(self):
            adminFile = open(adminPath, 'w')
            adminFile.write(json.dumps(self.admin, indent=4, cls=Encoder))
            adminFile.close()

    instance = None

    def __init__(self):
        if not Data.instance:
            Data.instance = Data._Data()


import json
from json import JSONEncoder

class Encoder(JSONEncoder):
    def default(self, _object):
        if isinstance(_object, Word):
            return {
                'uuid': _object.uuid, 
                'name': _object._name, 
                'translations': _object._translations
            }

        elif isinstance(_object, Translation):
            return {
                'uuid': _object.uuid,
                'text': _object.text,
                'language': _object.language
            }

        elif isinstance(_object, Language):
            return {
                'uuid': _object.uuid,
                'name': _object.name
            }

        elif isinstance(_object, Translator) or isinstance(_object, Admin):
            return {
                'createdWords': _object._createdWords,
                'name': _object._name,
                'password': _object._password,
                'translationRights': _object._translationRights,
                'translatedWords': _object._translatedWords
            }

        elif isinstance(_object, User):
            return {
                'createdWords': _object._createdWords
            }

from scripts.user import User
from scripts.translator import Translator
from scripts.admin import Admin
from scripts.word import Word
from scripts.translation import Translation
from scripts.language import Language