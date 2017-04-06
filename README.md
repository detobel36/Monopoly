# Etude du Monopoly via les chaînes de Markov
Ce projet comporte un rapport écrit décrivant les chaines de Markov, la modélisation
du Monopoly à travers des chaines de Markov et également les résultats obtenu grace à ce
"simulateur".

### Structure des fichiers
![Folder](https://filepursuit.com/__ovh_icons/folder.png) **App**            
L'application permettant de simuler l'évolution du monopoly.

![Folder](https://filepursuit.com/__ovh_icons/folder.png) **Rapport**            
Dossier contenant tous les fichiers permettant de générer le rapport.

![Folder](https://filepursuit.com/__ovh_icons/folder.png) **Ressource**            
Tous les documents (exclus donc ceux directement consulté sur internet) utilisé comme réference 
pour la réalisation de ce projet (les autres références se trouvent dans le rapport).

### Dépendances

**Python**               
Pour que le projet `Python` fonctionne il faut posséder la libraire `Tkinter` et également `numpy`
utilisé respectivement pour l'interface graphique et les calculs matriciel.


### Compliation
Seul le `LaTeX` doit être compilé.  Il est possible de le faire via le `Makefile` et la commande
suivante:
```
make rapport
```

### Utilisation de l'application
Pour lancer l'application il suffit de faire la commande suivante
```
App/python3 main.py
```

