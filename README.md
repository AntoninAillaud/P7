# Prédiction de scoring bancaire

Le but du projet est de créer une API qui va permettre de nous dire si un client peut obtenir un prêt bancaire ou non.
Traitement des données, feature engineering, comparaison de modèles de classification à l'aide d'un score métier puis sauvegarde du modèle finale.
Suite à ces étapes, la création d'une API qui va utiliser le modèles finale pour prédire ou non le prêt bancaire avec des données d'un client en particulier.
L'API est testée et déployée automatiquement sur un serveur Azure à l'aide des github actions.

Voici la description du repo et de ses fichiers :

+- API.ipynb                            - Le notebook de l'API qui a été utilisé avant la création du fichier "api.py"
+-  api.py                              - Le fichier python de l'API
+-  BEST_MODEL.sav                      - Le modèle utilisé par l'API pour la prédiction
+-  README.md                           - La description du repo
+-  requirements.txt                    - La liste des librairies python indispensables
+-  seuil.txt                           - Le seuil utilisé pour la prédiction avec le modèle
+-  test.csv                            - Les données utilisées pour la prédiction des clients
+-  test.py                             - Les tests unitaires de l'API
|
+---.github
|   \---workflows
|           master_predaaillaud.yml     - La description des actions githubs lors d'un push sur le repo
