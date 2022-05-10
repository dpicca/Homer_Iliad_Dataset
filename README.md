# Plato_Homer_Personality

## Contexte

Dans le cadre du cours de programmation pour le web sémantique, vous devrez prendre un jeu de données sur les dialogues de l'Iliade afin de saisir la personnalité et le rôle des personnages à travers des discours directs.
L'idée est pouvoir exploiter l'ontologie sortante afin de l'utiliser comme base pour la création d'avatars dans les jeux vidéos.

## Objectifs

Les objectifs du projet sont simples et peuvent être divisés en quatre étapes distinctes

- Nettoyer les données sources afin de les structurer dans un DataFrame.
- L'analyse et la création de statistiques sur ces données, comme par exemple celles décrites dans [cet article](./data/Annotating_the_Sentiment_of_Homeric_Text__LREC_2022_.pdf).
- Explorer et analyser les ontologies [character-profiling-ontology](https://github.com/dpicca/ontologies/tree/main/character-profiling-ontology/V2) ainsi que [lemon](https://lemon-model.net/)
- Modifier et créer des nouvelles régles SWRL de l'ontologie `character-profiling-ontology`
- Faire un alignement ontologique entre les deux ontologies
- Nourrir l'ontologie avec les données
- Créer des systèmes d'évaluations