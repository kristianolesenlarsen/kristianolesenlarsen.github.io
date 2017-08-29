---
title: Hvordan du får python
description: så du kan programmere for din arbejdsgiver
layout: default
---
# HOW TO GET PYTHON PÅ DANSK

## 1) Installer Conda
Installer MiniConda med python 3.x fra deres [downloadside](https://conda.io/miniconda.html) - conda kan holde styr på din pythoninstallation, og skal bruges til at installere pakker. (Du vil gerne tilføje conda til din system-PATH, selvom de fraråder det)

## 2) Installer Atom
Installer Atom fra deres [hjemmeside](http://atom.io/).

### 2.1)
Atom skal bruge en python-pakke der hedder `jupyter` og en Atom pakke der hedder `Hydrogen` for at køre python kode, start med at installere jupyter ved at åbne command-prompten (kør: cmd) og skriv

```
pip3 install --upgrade pip
pip3 install jupyter
```

Åben derefter Atom og vælg file > settings > install og søg efter 'Hydrogen', det skulle gerne se således ud:
![](hydr.png)

Det kan også anbefales at installere pakkerne `minimap` og `file-icons`i Atom, samt at ændre temaet fra mørkt til lyst.


## 3) Test at alt virker
Nu burde python køre på din computer. Næste skridt er at åbne Atom og lave en ny `.py` fil. Det nemmeste er at starte med at oprette en tom mappe på skrivebordet, og i Atom trykke `file > Open Folder` for at åbne mappen du lige har lavet. Højreklik på det grå område under mappen for at oprette en ny fil med navnet `HelloWorld.py`.

![](newfile.png)

Når du har lavet en `.py` fil er du klar til at skrive Python kode, start med at skrive `print(Hello World)`, marker teksten og tryk `ctrl`+`enter`. Der går lidt tid før Python er startet op, men så skulle koden gerne køre.

![](hello.png)


## 4) Lær Python

### 4.1) basics

Python bruger indryk til at signallere kodens hieraki, og kolon til at signalere begyndelsen på et indrykket kodestykke. Prøv for eksempel at køre

```python
for letter in ['a','b','c']:
  print(letter)
```

Python har flere forskellige datastrukturerer, vores udtryk ['a','b','c'] fra før kaldes en liste, men vi kan også have strenge, fx

```python
for letter in 'string':
  print(letter)
```

Eller dictionaries:

```python
dictionary = {'cat': 'good', 'dog': 'evil'}
for i in dictionary:
    print(i + "'s are " + dictionary[i])
```

Her har vi også anvendt at vi kan subsette datatyper med `[]`, for eksempel er `dictionary['cat'] = 'good'`. Lister kan subsettes efter deres index, så for eksempel er `[10,20,30][0] = 10` og `['a','b','c'][2] = 'c'`.


### 4.2) import og nye pakker

Python kan alt, men de fleste af de ting python kan, ville tage årtier at programmere selv. Derfor komme python med en række pakker, som udvider funtkionaliteten. Start med at prøve pakken `webbrowser`:

```python
import webbrowser

webbrowser.open('https://google.com')
```
De funktioner en pakke indeholder kaldes _methods_ og tilgås med punktum. For at vide hvad en pakke indeholder af funktionalitet er det som regel nødvendigt at google sig frem. For at undgå at skrive for meget, er det normalt at forkorte pakkernes navne når man importerer dem:


```python
import webbrowser as wb

wb.open('https://google.com')
```

Man kan også nøjes med at importere bestemte funktioner ved at skrive


```python
from webbrowser import open

open('https://google.com')
```

Der findes også en masse pakker der ikke kommer installeret som standard. De kan være lidt besværlige at installere, men de fleste kan fås ved at åbne command-prompten og skrive en af to følgende komandoer

```
pip install pakkenavn
conda install pakkenavn
```
Forsøg for eksempel at installere pakken `requests` med `pip`. Det kan godt betale sig at læse lidt op på Conda - bl.a. kan Conda nemlig holde styr på de pakker du installerer, og isolere dem i et virtuelt miljø, sådan at du har helt styr på hvilke versioner af forskellige pakker din kode virker med.


### 4.3) funktioner

Tit skal den samme opgave løses flere gange, det kunne for eksempel være at vi ville lave et program til at hente oplysninger fra statstidende. Så skal vi sandsynligvis gentagende gange kunne generere et link til deres ReST API (google hvad det er). Kodestykker vi vil kunne genbruges kaldes funktioner og defineres med `def`, for eksempel kan vi lave en lommeregner ved at skrive

```python

def calculator(a,b, operation = 'add'):
  if operation == 'add':
    return a+b
  elif operation == 'subst':
    return a-b
  elif operation == 'mult':
    return a*b
  elif operation == 'div':
    return a/b
  else:
    print('Not a valid operation')
    return None
```

Funktionen `calculator` tager tre inputs, `a`, `b` og variablen `operation`, som har `add` som default indstilling. Bemærk at der bruget et lig-med-tegn (=) til at definere værdien af en variable, mens to lig-med-tegn (==) tester om det passer at to størrelser er lig hinanden (`3==3` returnerer `True`, mens `3==4` returnerer `False`).

Efter at have defineret vores funktion i Python kan vi kalde den igen og igen [og...](https://www.youtube.com/watch?v=SMaVOcLHygE)

```python
calculator(3,4, 'add')       # returnerer 7
calculator(3,4,'mult')       # returnerer 12
```
Ligesom `return` er der en række andre nøgleord, som python reserverer, for eksempel `break`, `yield` og `continue` - dem kan man google hvordan virker.

### 4.4) strenge

Et af de dataformater man arbejder mest med er tekst. Det kan være man skal autoudfylde en mail,afgøre om en artikel indeholder et bestemt ord, eller alt muligt andet. I python angives en streng ved at omslutte teksten af enten `''` eller `""` Strenge kan subsettes med [] sådan at det første bogstav er `str[0]` osv, for eksempel er `'ABCDE[2] = 'C'`.

Den nemmeste måde at sammensætte strenge på er med `+`, det virker sådan at `'ABC'+ 'DE' = 'ABCDE'`. Hvis vi kender formattet på en streng, og skal udfylde den med variable kan vi bruge `''.format()`:

```python
import webbrowser as wb

def search_google(search_term):
  query = 'https://google.dk/search?q={}'.format(search_term)

  try:
    wb.open(query)

  except:
    print("Ooops, couldn't open google to search for '{}'".format(search_term))  
```
Her har vi også brugt `try` og `except`, som håndterer kode der _måske_ returnerer en fejl. Hvis vi kalder funktionen, fx med `search_google(bajer)` åbner python en webbrowser og søger på google.

Der er mange flere tricks med strenge, men som med alt andet er det nemmeste at lære det når man får brug for det.

# Klasser

Klasser fungerer lidt lige som funktioner, men en klasse kan indeholde flere funktioner, og er i det hele taget en mere kompliceret struktur. Klasser er en central struktur i 'rigtig' python programmering. Vi kan tænke på klasser som abstraktioner der hånterer de ting der er ens på tværs af klassens medlemmer. Et simpelt eksempel på en klasse kunne være en abstrakt studerende:

```python
class student():

  def __init__(self, skills, ambitions):
    self.skills = skills
    self.ambitions = ambitions

  def study(self, need_beer = True):
    if self.ambitions > self.skills:
        if need_beer:
            print("""I wont study today even though im behind
            on school, instead i'll go get a drink""")
            return False
        else:
            print("""I'm already studying since my skills
            don't match my ambitions, and i dont
            want beer right now""")
            return True
    else:
        print("""I have studied more than i had ambitions to do,
        i'll get a beer now""")
        return False

```
Her er `student()` en klasse, der indeholder en `__init__` funktion, som er en særlig funktion der kun køres første gang klassen kaldes, og en anden funktion `study()` der angiver om den studerende vil læse eller drikke øl.

Vi kan nu definere to studerende:

```python
Allan = student(skills = 10, ambitions = 3)
Bob = student(skills = 5, ambitions = 8)
```
For at finde ud af om Allan og Bob kan drikke øl sammen skal vi bruge en funktion der tager hver af deres præferencer som input, og som output giver `True` hvis de begge har lyst til at drikke øl:

```python
def beer_together(student1, student2):
  if not student1 and not student2:   #husk student.study() er true hvis den studerende IKKE vil drikke øl
    print('A and B can dring beer together')
    return True
  else:
    print('No beers tonight')
    return False
```
Nu kan vi afgøre om Allan og Bob vil drikke øl sammen på en aften hvor de begge to har lyst til øl, ved at skrive

```python
does_A_want_beer = Allan.study(need_beer = True)      # returnerer True
does_B_want_beer = Bob.study(need_beer = True)        # returnerer False

beer_together(does_A_want_beer, does_B_want_beer)    # returnerer False
```
Der er altså ingen fælles øl til Allan og Bob den aften.

## Klasser forsat

Tidligere lavede vi en funktion der fungerede som simpel lommeregner, men vi kunne forestille os en situation hvor det var upraktisk at skulle kalde funktionen igen og igen, for at skifte mellem plus og minus. Til det kan vi bruge klasser, vi begynder med at definere en meget simpelt lommeregnerfunktion:

```python
def calculator(a, b):
    return calcinternals(a, b)
```

Hvis vi kører denne funktion får vi en fejl, fordi `calcinternals` ikke er defineret - lad os lave en klasse med det navn:

```python
class calcinternals():
    def __init__(self, a, b):
        self.A = a
        self.B = b

    @property
    def sum(self):
        return self.A + self.B

    @property
    def difference(self):
        return self.A - self.B

    @property
    def product(self):
        return self.A * self.B

    @property
    def fraction(self):
        return self.A / self.B
```
Den nye klasse har en række `@property` definitioner - det er som navnet antyder properties. Nu returnerer `calculator` ikke et tal, men en _instance_ af klassen `calcinternals`. Vi kan tilgå de forskellige resultater på følgende måde:

```python
x = calculator(3,4)

x.sum         # returnerer 7
x.product     # returnerer 12
```
