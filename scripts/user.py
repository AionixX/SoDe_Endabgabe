class User():
    def __init__(self, _createdWords):
        self._createdWords = _createdWords

    def PrintContext(self):
        print(
'''
Enter the number to use the function. Enter nothing to quit the programm.
    1: Search for a word
    2: Get created words
    3: Get number of created words
    4: Get number of total words in database
    5: Login
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
            login = self.Login()
            if login:
                return False
        else:
            return True

        print('')
        input('Type anything to return to the menu')
        return False

    def SearchWord(self):
        wordToSearch = input('Type in the word: ')
        wordToSearch
        print('')

        foundWord = False
        for word in Data.instance.words:
            if word.GetName().lower() == wordToSearch.lower():
                foundWord = True
                for language in Data.instance.languages:
                    translation = self.FindTranslation(language, word.GetTranslations())
                    print('{}: {}'.format(language.name, translation.text))

        if not foundWord:
            print('Sorry we haven\'t found the word you are looking for.')
            create = input('Do you want to create it? [y] / [n]')
            if create == 'y':
                newUUID = str(uuid.uuid4())
                newWord = Word(newUUID, wordToSearch, [])
                self._createdWords.append(newWord.uuid)
                Data.instance.words.append(newWord)
                Data.instance.SaveData()

        print('')
        again = input('Want to search another word? [y] / [n]')
        if again == 'y':
            self.SearchWord()

    def FindTranslation(self, _language, _translations):
        for translation in _translations:
            if translation.language == _language.uuid:
                return translation
        
        return NullTranslation()

    def FindWord(self, _uuid):
        for word in Data.instance.words:
            if word.uuid == _uuid:
                return word

    def PrintCreatedWords(self):
        if len(self._createdWords) <= 0:
            print('Sorry but you haven\'t created words yet.')
        else:
            counter = 1
            for word in self._createdWords:
                wordToFind = self.FindWord(word)
                print('{} : {}'.format(counter, wordToFind.GetName()))
                counter = counter + 1

    def PrintNumberOfCreatedWords(self):
        number = len(self.GetCreatedWords())
        if number <= 0:
            print('You haven\'t translated words yet')
        else:
            print('You have created {} {}'.format(number, "word" if number == 1 else "words"))

    def PrintTotalNumberOfWords(self):
        count = len(Data.instance.words)
        fullyTranslated = self.GetNumberOfFullyTranslatedWords()
        print('There are {} words in the database. {} of them are fully translated'.format(count, fullyTranslated))


    def GetNumberOfFullyTranslatedWords(self):
        counter = 0
        for word in Data.instance.words:
            if len(Data.instance.languages) == len(word.GetTranslations()):
                counter = counter + 1

        return counter

    def Login(self):
        username = input('Username: ')
        password = input('Password: ')

        successTranslator = Data.instance.translator.CheckCredetials(username, password)
        successAdmin = Data.instance.admin.CheckCredetials(username, password)

        if successTranslator or successAdmin:
            Data.instance.activeUser = Data.instance.translator if successTranslator else Data.instance.admin
            print('Successfully logged in as {}'.format(Data.instance.activeUser._name))
            return True
        else:
            print('Wrong Credetials!')
            again = input('Want to try again? [y] / [n] ')

            if again == 'y':
                return self.Login()
            else:
                return False

    def GetAllWords(self): return Data.instance.words

    def GetName(self): return self._name

    def SetName(self, _newName): self._name = _newName

    def GetCreatedWords(self): return self._createdWords

from .data import Data
from .word import Word
from .nullTranslation import NullTranslation
import uuid