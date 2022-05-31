# Plato_Homer_Personality


## Installer les dépendances

```
pip install -r requirements.txt
```
## Données requises

Si vous souhaitez ajouter des données à l'ontologie, il vous sera nécessaire de les acquérir sous format JSON, labélisées de manière similaire aux fichiers que vous pouvez trouver dans le dossier Dataframes/Jsonfiles. Le logiciel utilisé pour réaliser ces fichiers est appelé [LabelStudio](https://labelstud.io/)

## Nettoyage de données

Vous trouverez dans le dossier "Dataframes" un document contenant un fichier "Data_cleaning.ipynb". Ce fichier contient des fonctions Python permettant de préparer des données afin qu'elles puissent ensuite être importées dans une ontologie sous forme de DataFrame.

Pour utiliser ce script, il vous suffit de fournir une liste de chemins vers les fichiers JSON contenant les données que vous souhaitez nettoyer:
```
json_list = ['Jsonfiles/ch1_1.json', 'Jsonfiles/ch1_2.json', 'Jsonfiles/ch1_3.json']
```
Il vous faut ensuite passer cette liste à travers la fonction merge_dataframes():
```
dataframe, krippendorff, graph = merge_dataframes(json_list)
```
Vous pourrez ensuite accéder au dataframe final, obtenir la valeur krippendorff du dataframe, et retrouver un graphique de vos données à l'aide des 3 variables ci-dessus.

## Contributors

- [Loïc Aubrays](https://ch.linkedin.com/in/loicaubrays), étudiant
- Gislain Delavy, étudiant
- [Marcela Hitrackova](https://ch.linkedin.com/in/marcela-hitrackova-2aa566222), étudiant
- [Davide Picca](https://www.unil.ch/unisciences/davidepicca), enseignant
