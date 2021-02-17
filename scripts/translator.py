import uuid
import re
from .user import User
from .data import Data
from .translation import Translation

class Translator(User):
    def __init__(self, _createdWords, _name, _password, _translationRights, _translatedWords):
        super().__init__(_createdWords)
        self._name = _name
        self._password = _password
        self._translationRights = _translationRights
        self._translatedWords = _translatedWords

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
    8: Logout
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
            self.Logout()
        else:
            return True

        print('')
        input('Type anything to return to the menu')
        return False

    def CheckCredetials(self, _username, _password):
        if _username == self._name and _password == self._password:
            return True
        else:
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
        for right in self._translationRights:
            if not self.HasWordTranslation(_word, right):
                translation = input('Type in the {} translation: '.format(self.GetLanguageName(right)))
                newUUID = str(uuid.uuid4())
                newTranslation = Translation(newUUID, translation, right)
                self._translatedWords.append(newTranslation.uuid)
                _word.AddTranslation(newTranslation)
                Data.instance.SaveData()
    
    def PrintNumberOfTranslatedWords(self):
        number = len(self._translatedWords)
        if number <= 0:
            print('You haven\'t translated words yet')
        else:
            print('You have translated {} {}'.format(number, "word" if number == 1 else "words"))

    def GetLanguageName(self, _uuid):
        for language in Data.instance.languages:
            if language.uuid == _uuid:
                return language.name

    def FindUntranslatedWords(self):
        words = []
        for word in Data.instance.words:
            canBeTranslated = False
            for language in self._translationRights:
                if not self.HasWordTranslation(word, language):
                    canBeTranslated = True
            if canBeTranslated:
                words.append(word)
        
        return words

    def HasWordTranslation(self, _word, _translation):
        for translation in _word.GetTranslations():
            if translation.language == _translation:
                return True
        
        return False
    
    def HasTranslationRight(self, _uuid):
        for right in self._translationRights:
            if right == _uuid:
                return True

        return False

    def AddTranslationRight(self, _uuid):
        self._translationRights.append(_uuid)

    def RemoveTranslationRight(self, _uuid):
        self._translationRights.remove(_uuid)
    
    def GetTranslationPercentage(self, _word):
        percentage = (len(_word.GetTranslations()) / len(Data.instance.languages))
        return '{:.0%}'.format(percentage)

    def ChangePassword(self):
        print('Note that the password needs to have minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character!')
        newPassword = input('Type in the new password: ')
        pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if re.match(pattern, newPassword):
            self._password = newPassword
            Data.instance.SaveData()
            print('You successfully changed your password!')
        else:
            print('The input is invalid!')
            again = input('Do you want to try again? [y] / [n]')
            if again == 'y':
                self.ChangePassword()


    def Logout(self):
        Data.instance.activeUser = Data.instance.user
        print('Successfully logged out')

    def GetTranslationRights(self): return self._translationRights