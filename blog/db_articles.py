# Création d'une liste d'articles
articles = [
    {
        "titre": "Introduction à Python",
        "date": "2024-01-10",
        "contenu": "Cet article présente les bases de Python, y compris les types de données, les boucles et les fonctions."
    },
    {
        "titre": "Les bibliothèques Python essentielles",
        "date": "2024-02-15",
        "contenu": "Découvrez les bibliothèques incontournables comme NumPy, Pandas et Matplotlib pour l'analyse de données."
    },
    {
        "titre": "Développement Web avec Flask",
        "date": "2024-03-20",
        "contenu": "Un guide pas à pas pour créer une application Web simple en utilisant le framework Flask."
    },
    {
        "titre": "L'apprentissage automatique avec Scikit-learn",
        "date": "2024-04-25",
        "contenu": "Introduction à l'apprentissage automatique et comment utiliser Scikit-learn pour construire des modèles."
    },
    {
        "titre": "Automatisation des tâches avec Python",
        "date": "2024-05-30",
        "contenu": "Apprenez à automatiser des tâches répétitives grâce à des scripts Python simples."
    }
]

# Affichage des articles
for article in articles:
    print(f"Titre: {article['titre']}\nDate: {article['date']}\nContenu: {article['contenu']}\n")