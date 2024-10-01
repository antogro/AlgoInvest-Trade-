# P7 AlgoInvest-Trade
# Optimisation d'Investissement des Actions

Cette application Python aide à optimiser les investissements en actions en utilisant différents algorithmes (brute force, glouton). Elle analyse un ensemble d'actions à partir d'un fichier CSV et suggère la meilleure combinaison d'actions à acheter en fonction d'un budget donné.

## Fonctionnalités

- Analyse des données d'actions à partir de fichiers CSV
- Implémentation d'un algorithme glouton pour la sélection d'actions
- Implémentation d'un algorithme de force brute pour trouver la combinaison optimale
- Calcul et affichage du coût total, du bénéfice total et des actions sélectionnées

## Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/antogro/P7-AlgoInvest-Trade.git
   cd P7-AlgoInvest-Trade

   ```

2. Assurez-vous d'avoir Python 3.7+ installé.

3. Aucune bibliothèque supplémentaire n'est requise car le projet n'utilise que les bibliothèques standard de Python.

## Utilisation

L'application fournit deux scripts principaux :

1. Algorithme Glouton (`optimized.py`)
2. Algorithme de Force Brute (`brute_force.py`)

### Algorithme Glouton

Exécutez l'algorithme glouton avec :

```
python optimized.py <chemin_vers_fichier_csv> <budget>
```

Exemple :
```
python optimized.py actions.csv 500
```

### Algorithme de Force Brute

Exécutez l'algorithme de force brute avec :

```
python brute_force.py <chemin_vers_fichier_csv> <budget>
```

Exemple :
```
python brute_force.py actions.csv 500
```

## Format du Fichier d'Entrée

Le fichier CSV doit avoir le format suivant :

```
action,cost,percent
Action1,10,5%
Action2,15,10%
...
```

- `action` : Nom de l'action
- `cost` : Coût de l'action
- `percent` : Pourcentage de rendement attendu

## Sortie

L'application affichera :
- Les actions sélectionnées avec leurs détails (nom, coût, bénéfice)
- Le coût total des actions sélectionnées
- Le bénéfice total
- Le nombre d'actions sélectionnées (pour l'algorithme optimizé)

## Structure du Projet

- `action_object.py` : Contient la définition de la classe `Action`
- `greedy_algo.py` : Implémente l'algorithme glouton
- `brute_force.py` : Implémente l'algorithme de force brute

## Auteurs

[antogro](https://github.com/antogro).