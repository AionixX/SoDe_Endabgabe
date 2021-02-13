# Softwaredesign WS20/21 Endabgabe

**Vorgelegt**: Dennis Hawran

**Matrikelnummer**: 262357

**Programmiersprache** Python

**Aufgabe**: TranslationMemory

## Inhaltsangabe

- [Installation](#Installation)
- [Konzeption](#Conception)
    - [UseCase Diagramm](#UseCase)
    - [Klassen Diagramme](#Class)
    - [Aktivitäts Diagramm](#Activity)
- [Aufgabe](#Task)
- [Allgemeine Anforderungen](#General)

<a name=Installation></a>

## Installation

**Wichtig:** Um das Programm ausführen zu können muss auf dem Zielrechner Python 3.7 oder höher installiert sein.

1. Das Repository clonen
* `git clone https://github.com/AionixX/SoDe_Endabgabe.git`
2. In den Ordner navigieren
* `cd ./SoDe_Endabgabe`
3. Die `main.py` starten
* `python main.py`

<a name=Conception></a>

## Konzeption

<a name=UseCase></a>

### UseCase Diagramm
![UseCase Diagram](./conception/Softwaredesign_Endabgabe-UseCase.svg)

<a name=Class></a>

### Klassen Diagramme
![UseCase Diagram](./conception/Softwaredesign_Endabgabe-ClassDiagramms.svg)

<a name=Activity></a>

### Aktivitäts Diagramme
![UseCase Diagram](./conception/Softwaredesign_Endabgabe-ActivityDiagramms.svg)

<a name=Task></a>

## Aufgabe

Mit Übersetzer, Admin und User sind sowohl männliche als auch weibliche Personen gemeint.

Aufgabe Übersetzungen Datenbank:

Zum Nachschlagen von Übersetzungen einzelner Wörter in anderen Sprachen soll eine Software Applikation aufgebaut werden.
Für diese Art von Applikation soll es drei unterschiedliche Rollen geben, den User, der Übersetzer und den Admin.

Der User kann nach Wörtern suchen und bekommt dann die Übersetzungen in den vorhandenen Sprachen, 
sofern die Übersetzung dafür vorhanden ist. Ansonsten wird an der Sprache der Text (Keine) angezeigt, bspw.:

Deutsch: Wasser
English: Water
Italiano: Acqua
Español: (Keine)

Der Einfachheit halber hat jedes Wort in jeder Sprache nur eine Übersetzung, auch wenn das faktisch falsch ist, 
wie am Beispiel Schloss erkennbar:

- Schloss (deutsch)
- Castle (english)
- Palace (english)
- lock (english)

Wenn ein Benutzer ein Wort sucht, dieses allerdings nicht vorhanden ist, hat dieser die Möglichkeit das Wort anzulegen.
Ein Wort besteht aus einer ID und dem Wort. Wörter bestehen lediglich aus Buchstaben. 
Am User soll gespeichert werden, wie viele Wörter dieser angelegt hat.
Der User hat die Möglichkeit sich anzeigen zu lassen, wie viele Wörter dieser angelegt hat.
Der User hat die Möglichkeit anzeigen zu lassen, wie viele Wörter insgesamt in der Datenbank vorhanden sind.
Dabei soll ebenso angezeigt werden, wie viele davon zu 100%, also in allen Sprachen, übersetzt sind.

Ein Übersetzer hat die Möglichkeit sich Wörter auflisten, bei denen Übersetzungen fehlen.
Bei der Auflistung der Wörter wird der prozentuale Grad der vorhandenen Übersetzungen anzeigt, bspw.:

- Wasser (66 %)

Für die einzelnen Wörter kann der Übersetzer dann in den jeweiligen Sprachen, die Übersetzung einpflegen.
Wenn ein Wort in allen Sprachen übersetzt ist, wird das Wort nicht in der Auflistung gezeigt.
Übersetzer haben lediglich die Möglichkeit die Übersetzungen für die Sprachen einzupflegen, für welche sie berechtigt sind.
Am Übersetzer soll dauerhaft gespeichert werden, wie viele Übersetzungen dieser eingepflegt hat.
Der Übersetzer kann sich diese Zahl anzeigen lassen.
Inhaltlich hat der Übersetzer ebenso die gleichen Möglichkeiten wie der User.

Der Übersetzer muss sich entsprechend an der Software anmelden können, hierfür benötigt der Admin einen Benutzernamen
und ein Passwort. Für das Anmelden an der Applikation reicht lediglich eine Eingabemaske mit 
Benutzername und Passwort. Benutzername und Passwort können hardcodiert im Quellcode überprüft werden, bspw. (translator/9876).

Der Admin hat die Möglichkeit neue Sprachen für die Applikation anzulegen und nach Wörtern und deren Übersetzungen zu suchen.
Darüber hinaus ist der Admin berechtigt dem Übersetzer eine Sprache zuzuweisen. Damit dieser Übersetzungen einpflegen kann.
Eine Sprache hat eine eindeutige ID und einen Namen.

Der Admin muss sich entsprechend an der Software anmelden können, hierfür benötigt der Admin einen Benutzernamen
und ein Passwort. Für das Anmelden an der Applikation reicht lediglich eine Eingabemaske mit 
Benutzername und Passwort. Benutzername und Passwort können hardcodiert im Quellcode überprüft werden, bspw. (admin/1234).

Die Loginmaske ist für den Übersetzer und den Admin genau dieselbe, lediglich über den Benutzer wird ermittelt, 
welcher Benutzertyp angemeldet ist.

<a name=General></a>

## Allgemeine Anforderungen

1. Es müssen drei UML-Diagramme erstellt werden:

    * :white_check_mark: Ein UseCase Diagramme

    * :white_check_mark: Ein Aktivitätsdiagramm eines UseCases aus dem UseCase Diagramm

    * :white_check_mark: Ein Klassendiagramm der Software

2. Quellcode:

    * :white_check_mark: Der Quellcode der Software muss objektorientiert entwickelt sein.

    * :white_check_mark: Die Software soll als Konsolenprogramm umgesetzt sein, ersatzweise als Browser Applikation.

    * :white_check_mark: Innerhalb des Quellcodes und Klassendiagramms müssen mindestens zwei Design Patterns eingearbeitet sein, gerne auch mehr.

        >Ein Singleton für das Datenobject und ein NullObject wenn es keine Übersetzung gibt

    * :white_check_mark: Innerhalb des Quellcodes soll es mindestens eine Umsetzung einer Regular Expression geben.

        >Die Regular Expressions wurdem benutzt um sicher zustellen das dass Passwort mindestens ein Großbuchstaben, ein Kleinbuchstaben, eine Zahl und ein Sonderzeichen besitzt

    Note: Am besten hierfür sind Eingaben von Zahlen, Nummern, Postleitzahlen, Namen, Texte, etc. geeignet.

3. Datenhaltung:

    * :white_check_mark: Die Daten müssen in Dateien im JSON oder XML Format gespeichert werden. Für die Objektstrukturen werden keine Vorgaben gemacht.

        >JSON

    * :white_check_mark: Es kann sinnvoll sein, die zu persistierenden Daten in unterschiedlichen Dateien zu speichern.

        >Der User, Translator, Admin und Sprachen haben jeweils eine eigene Datei. Die Wörter in der Datenbank und ihre Übersetzungen sind in einer Datei da eine Übersetzung nicht ohne ihr Wort existieren kann

    * :white_check_mark: Bei 1:1 Relationen der Daten zueinander können diese als eigene Attribute an den Datenobjekten gespeichert werden. 

    * :white_check_mark: Bei 1:N und N:N Relationen der Daten zueinander kann es Sinn machen, diese in eigenen Daten abzuspeichern. Stichwort Zwischentabelle

    * :white_check_mark: Aus dem Programm heraus müssen neue Daten angelegt werden können und in die bestehenden Dateien gespeichert werden.

    * :white_check_mark: Aus dem Programm heraus müssen die Daten aus den Dateien gelesen werden. 

    * :white_check_mark: Jeder Datensatz muss eindeutig sein, über Vor- und Nachname lässt sich keine Eindeutigkeit herstellen.

        >Alle Wörter und Übersetzungen besitzen eine uuid. User, Translator und Admin besitzen einen Nutzernamen

    Note: Bitte beachten Sie hierzu die Möglichkeiten aus der Vorlesung (Spezifisches Attribut, Fortlaufende Nummer oder UUID)

Sprache:

- :white_check_mark: Der gesamte Quellcode muss in Englisch sein 

- :white_check_mark: UseCase Diagramm und Aktivitätsdiagramm können in Deutsch sein, Klassendiagramm in Englisch für die Synergie zum Quellcode

Hinweise:

- :white_check_mark: Bitte beachtet die Regeln aus dem Kapitel 04 Clean Code

- :white_check_mark: Bitte denkt daran euch eigene Code Konventionen zu setzen und diese im Quellcode konsequent umzusetzen

    >Im kompletten Quellcode wurde CamelCase benutzt, jedoch bei Klassen und Methoden mit einem Großbuchstaben am Anfang.
    >Übergabepparameter bekommen einen Unterschrich am Anfang.

    >Da Python das Konzept der Privaten und Öffentlichen Instanzvariablen nicht kennt wurde dies über die Konventionen gelöst.
    >Öffentliche Variablen werden ganz normal in CamelCase gerschrieben und Private oder geschütze Variablem mit einem Unterstrich am Anfang.
    >Dies hält zwar nicht davon ab 'Private' Member zu benutzen, soll jedoch daran Errinern das es nicht getan werden sollte.

- :white_check_mark: Bitte achtet auf eine gewisse Modularisierung in eurem Quellcode

- :white_check_mark: Seit entsprechend kreativ, wenn es darum geht, welche Attribute und Methoden bei den Klassen Sinn macht.

- :white_check_mark: Attribute und Methoden können entsprechend sinnvoll sein, auch wenn diese nicht direkt aus dem Aufgabentext ersichtlich sind.