# Générer le fichier PDF avec Pandoc

## Installation

Installer [Pandoc](https://pandoc.org/installing.html) pour convertir le document d'un format à l'autre et [Pandoc-crossref](https://github.com/lierdakil/pandoc-crossref#installation) pour numéroter les éléments et les référencer.

## Générer le document

Dans un terminal, se placer dans le dossier *report* puis
```
pandoc --filter pandoc-crossref myReport.md -o myReport.pdf
```
