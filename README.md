# Rapports Géofluence

Cette extension QGIS permet de générer des rapports aux formats word depuis les formulaires de Géofluence.

## Fonctionnement

Vous devez d'abord sélectionner un rapport à remplir depuis le menu des extensions. Chaque rapport est associé à un formulaire spécifique. Seuls les rapports pour lesquels le formulaire est présent dans le projet actif sont proposés à l'utilisateur.

On vous demande de choisir un projet ou une période pour sélectionner les entités à inclure dans le rapport. Les projets et les dates proviennent de la couche Événement, qui doit aussi se trouver dans le projet actif pour assurer le fonctionnement.

![image](./plugin.jpg)

## Installation des dépendances

Pour générer des rapports au format Word, vous devez installer certains packages dans l'environnement de QGIS.

Pour ce faire, copier simplement le contenu du dossier "packages" dans le dossier site-packages de QGIS, sur votre poste de travail : "C:\Program Files\QGIS 3.40.11\apps\Python312\Lib\site-packages".

Redémarrer QGIS pour activer les nouveaux packages.

Une fois les packages installés, vous n'avez plus besoin du dossier "packages". Vous pouvez l'effacer.

## Pour les photos

Pour que les photos prises à partir des formulaires apparaissent dans les rapports, un dossier DCIM doit exister au même endroit que le projet QGIS actif. 

Placer vos fichiers photos dans ce dossier en vous assurant que les noms des fichiers correspondent à ceux qu'on retrouve dans le formulaire. Si vous n'avez pas modifié les noms des fichiers après la collecte des données, vous ne devriez pas rencontrer de problème.