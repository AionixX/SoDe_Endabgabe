import uuid
from .translator import Translator
from .data import Data
from .translation import Translation
from .language import Language

class Admin(Translator):
    def __init__(self, _createdWords, _name, _password, _translationRights, _translatedWords):
        super().__init__(_createdWords, _name, _password, _translationRights, _translatedWords)

    def PrintContext(self):
        print(
'''
Enter the number to use the function. Enter nothing to quit the programm.
    1: Search for a word
    2: Get created words
    3: Get number of created words
    4: Get number of total words in database
    5: Show untranslated words
    6: Show number of translated words
    7: Change password
    8: Add new Language
    9: Change translator rights
    0: Logout
'''
        )
        userInput = input('Choose function: ')

        if userInput == '1':
            self.SearchWord()
        elif userInput == '2':
            self.PrintCreatedWords()
        elif userInput == '3':
            self.PrintNumberOfCreatedWords()
        elif userInput == '4':
            self.PrintTotalNumberOfWords()
        elif userInput == '5':
            self.PrintUntranslatedWords()
        elif userInput == '6':
            self.PrintNumberOfTranslatedWords()
        elif userInput == '7':
            self.ChangePassword()
        elif userInput == '8':
            self.AddNewLanguage()
        elif userInput == '9':
            self.ChangeTranslatorRights()
        elif userInput == '0':
            self.Logout()
        else:
            return True

        print('')
        input('Type anything to return to the menu')
        return False

    def PrintUntranslatedWords(self):
        untranslatedWords = self.FindUntranslatedWords()
        counter = 1
        for word in untranslatedWords:
            print('{}: {} ({})'.format(counter, word.GetName(), self.GetTranslationPercentage(word)))
            counter = counter + 1

        print('')

        wantToTranslate = input('Type in the number you want to translate. Type nothing to return to menu: ')
        if not wantToTranslate == '':
            number = int(wantToTranslate) - 1
            if number < len(untranslatedWords):
                self.TranslateWord(untranslatedWords[number])
                self.PrintUntranslatedWords()
            else:
                input('The input was invalid! Please hit enter and try again')
                self.PrintUntranslatedWords()  
    
    def TranslateWord(self, _word):
        for language in Data.instance.languages:
            if not self.HasWordTranslation(_word, language.uuid):
                translation = input('Type in the {} translation: '.format(language.name))
                newUUID = str(uuid.uuid4())
                newTranslation = Translation(newUUID, translation, language.uuid)
                self._translatedWords.append(newTranslation.uuid)
                _word.AddTranslation(newTranslation)
                Data.instance.SaveData()
    
    def FindUntranslatedWords(self):
        words = []
        for word in Data.instance.words:
            if len(Data.instance.languages) > len(word.GetTranslations()):
                words.append(word)
        
        return words

    def AddNewLanguage(self):
        newLanguageName = input('Type in the name of the new Language: ')
        newUUID = str(uuid.uuid4())
        newLanguage = Language(newUUID, newLanguageName)
        Data.instance.languages.append(newLanguage)
        Data.instance.SaveData()

    def ChangeTranslatorRights(self):
        action = input('Do you want to add [a] or delete [d] rights from the translator? Type anything else to return')
        if action == 'a':
            self.AddRightToTranslator()
        else:
            self.DeleteRightOfTranslator()

    def AddRightToTranslator(self):
        possibleLanguages = []
        for language in Data.instance.languages:
            if not Data.instance.translator.HasTranslationRight(language.uuid):
                possibleLanguages.append(language)

        if len(possibleLanguages) <= 0:
            print('The translator has no rights!')
            return
        
        counter = 1
        for language in possibleLanguages:
            print('{}: {}'.format(counter, possibleLanguages[counter - 1].name))
            counter = counter + 1
        
        action = input('Type in the number of which language you want to add to the translator: ')
        action = int(action) - 1

        if action > len(possibleLanguages):
            print('Sorry the input was invalid!')
            return
        
        Data.instance.translator.AddTranslationRight(possibleLanguages[action].uuid)
        Data.instance.SaveData()
        print('Successfully added right to translator!')
    
    def DeleteRightOfTranslator(self):
        translationRights = Data.instance.translator.GetTranslationRights()

        if len(translationRights) <= 0:
            print('There is nothing to delete')
            return
    
        counter = 1
        for right in translationRights:
            print('{}: {}'.format(counter, self.GetLanguageName(right)))

        action = input('Which one do you want to delete? Enter nothing to cancle')

        if action == '':
            return

        action = int(action) - 1

        if action > len(translationRights):
            print('Sorry the input was invalid!')
            return

        Data.instance.translator.RemoveTranslationRight(translationRights[action])
        Data.instance.SaveData()
        print('Successfully deleted right of translator!')

