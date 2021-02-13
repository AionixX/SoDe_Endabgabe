from scripts.language import Language
from scripts.nullTranslation import NullTranslation
from scripts.translation import Translation
from scripts.user import User
from scripts.data import Data

def __init__():
    Data()
    Menu()

def Menu():
    wantToQuit = Data.instance.activeUser.PrintContext()

    if wantToQuit == False:
        Menu()

__init__()