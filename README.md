Budget App :
Application console simple pour calculer et sauvegarder un budget mensuel

📌 Présentation :
Budget App est une petite application Python en ligne de commande permettant de :
- saisir un revenu mensuel,
- entrer des dépenses par catégorie,
- calculer automatiquement le total des dépenses et les économies restantes,
- sauvegarder toutes les données dans un fichier JSON (data/finances.json).
L’objectif est de fournir un outil minimaliste, rapide et extensible pour suivre un budget mensuel.

📂 Fonctionnalités :
- Saisie interactive du revenu et des dépenses.
- Calcul automatique :
- total des dépenses,
- économies restantes.
- Sauvegarde persistante dans un fichier JSON.
- Structure simple permettant d’ajouter facilement d’autres catégories ou fonctionnalités.

🛠️ Installation
1. Cloner ou télécharger le projet
Place le script Python dans un dossier de ton choix.

2. Vérifier la présence de Python
L’application fonctionne avec Python 3.x.
python --version

3. Lancer l’application
python app.py

▶️ Utilisation
Lors de l’exécution, l’application te demande :
- Ton revenu mensuel
- Tes dépenses dans les catégories suivantes :
- Loyer (rent)
- Nourriture (food)
- Factures (utilities)
- Loisirs (leisure)
Une fois les valeurs saisies, elle affiche :
- le revenu total,
- les dépenses totales,
- les économies restantes.
Puis elle sauvegarde automatiquement les données dans :
data/finances.json



