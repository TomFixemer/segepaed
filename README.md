# Sexualisierte Gewalt gegen Kinder und Jugendliche in pädagogischen Kontexten

## Zur Installation benötigte Programme

Um unseren Workflow zu wiederholen sind bestimmte Programme notwending, vor allem `git`, und `python3`. 
Um zu beginnen, muss dieses Repository "geklont" werden. Dies geschieht mit Hilfe von `git` im Terminal durch den Befehl:

```shell
$ git clone https://github.com/SeGePae/segepaed.git
```

Jetzt, wo dies getan wurde, können wir mit `cd` in diesen Ordner wechseln.

```shell
$ cd segepaed
```

In order to propose changes, for example, on the bibliography, you can use the following command:

```shell
$ git add data/*.bib
```
We assume here that the bibliography files are in the folder `data` and end in `.bib`.

To store a version of your data, you must `commit` them:

```shell
$ git commit -m "first commit"
```

In order to use the Python scripts, you need Python in version 3. You will also need the `pip` program in order to install Python packages.

```shell
$ pip install -r requirements.txt
```

Once this has been done, you can start to convert the data to the website.

We start by normalizing the LaTeX code in the bibtex file:

```shell
$ python normalize.py data/Bibliographie.tsv
```

This creates a new file `data/Bibliographie-normalized.tsv`.

With this file, and the file with the additional information on the `Laufnummer`, which needs to be replaced in `data/laufnummern.tsv`, you can now run the script that parses the data.

```shell
$ python parse.py
```

With this, we can now finally create the website:

```shell
$ python make-page.py
```

The website is now in `segepaed/index.html`, where it can be opened by double-clicking.
