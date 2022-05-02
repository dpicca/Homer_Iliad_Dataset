# Plato_Homer_Personality

## Contexte

Dans le cadre du cours de programmation pour le web sémantique, vous devrez prendre un jeu de données sur les dialogues de l'Iliade afin de saisir la personnalité et le rôle des personnages à travers des discours directs.

## Objectifs

Les objectifs du projet sont simples et peuvent être divisés en quatre étapes distinctes

- Nettoyer les données sources afin de les structurer dans un DataFrame.
- L'analyse et la création de statistiques sur ces données, comme par exemple celles décrites dans [cet article](Annotating_the_Sentiment_of_Homeric_Text__LREC_2022_.pdf).
- Explorer et analyser les ontologies [character-profiling-ontology](https://github.com/dpicca/ontologies/tree/main/character-profiling-ontology/V2)
  -  vous trouverez plus d'infos sur cet ontologie [ici](An_Ontological_Model_for_Inferring_Psychological_Profiles_and_Narrative_Roles_of_Characters.pdf) 
- ainsi que [ontolex-lemon](https://raw.githubusercontent.com/ontolex/lexinfo/master/ontology/3.0/lexinfo.owl)
  - vous trouverez plus d'infos sur cet ontologie [ici](https://www.w3.org/2019/09/lexicog/), [ici](https://lemon-model.net/index.php), [ici](https://elex.link/elex2017/wp-content/uploads/2017/09/paper36.pdf) et [ici](https://youtu.be/TxqvnLPIsa8)
- Modifier et créer des nouvelles régles SWRL de l'ontologie `character-profiling-ontology`
- Faire un alignement ontologique entre les deux ontologies
- Nourrir l'ontologie avec les données
- Créer des systèmes d'évaluations
