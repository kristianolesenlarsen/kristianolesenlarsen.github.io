---
title: Hvordan du får python
description: så du kan programmere for din arbejdsgiver
layout: default
---

## 1) Installer Conda
Installer MiniConda med python 3.x fra deres [downloadside](https://conda.io/miniconda.html) - conda kan holde styr på din pythoninstallation, og skal bruges til at installere pakker. (Du vil gerne tilføje conda til din system-PATH, selvom de fraråder det)

## 2) Installer Atom
Installer Atom fra deres [hjemmeside](http://atom.io/)

### 2.1)
Atom skal bruge en python-pakke der hedder `jupyter` og en Atom pakke der hedder `Hydrogen` for at køre python kode, start med at installere jupyter ved at åbne command-prompten (kør: cmd) og skriv

```
pip3 install --upgrade pip
pip3 install jupyter
```

Åben derefter Atom og vælg file > settings > install og søg efter 'Hydrogen', det skulle gerne se således ud:
![](hydr.png)

Det kan også anbefales at installere pakkerne `minimap` og `file-icons`, samt at ændre temaet fra mørkt til lyst.


## 3) Test at alt virker
Nu burde python køre på din computer. Næste skridt er at åbne Atom og lave en ny `.py` fil. Det nemmeste er at starte med at oprette en tom mappe på skrivebordet, og i Atom trykke `file > Open Folder` for at åbne mappen du lige har lavet. Højreklik på det grå område under mappen for at oprette en ny fil med navnet `HelloWorld.py`.

![](newfile.png)

Når du har lavet en `.py` fil er du klar til at skrive Python kode, start med at skrive `print(Hello World)`, marker teksten og tryk `ctrl`+`enter`. Der går lidt tid før Python er startet op, men så skulle koden gerne køre.

![](hello.png)

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

Eller dictionaries, som har formattet

```python
dictionary = {'cat':'good', 'dog': 'evil'}
for i in dictionary:
    print(i + "'s are " + dictionary[i])
```

Her har vi også anvendt at vi kan subsette datatyper med `[]`, for eksempel er `dictionary['cat'] = 'good'`. Lister kan subsettes efter deres index, så for eksempel er `[10,20,30][0] = 10` og `['a','b','c'][2] = 'c'`. 
