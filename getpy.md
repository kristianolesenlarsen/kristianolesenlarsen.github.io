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

### 4.1)
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



### 4.2)

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


Der findes også en masse pakker der ikke kommer installeret som standard. De kan være lidt besværlige at installere, men de fleste kan fås ved at åbne command-prompten og skrive en af to følgende komandoer
```
pip install pakkenavn
conda install pakkenavn
```
Forsøg for eksempel at installere pakken `requests` med `pip`.


### 4.3)
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

Efter at have defineret vores funktion i Python kan vi kalde den igen og igen

```python
calculator(3,4, 'add')       # returnerer 7
calculator(3,4,'mult')       # returnerer 12
```
