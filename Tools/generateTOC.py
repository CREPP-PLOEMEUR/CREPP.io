import re

def generate_markdown_toc(file_path):
    try:
        # Ouvrir le fichier Markdown et lire son contenu
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Rechercher la section de sommaire existante
        toc_regex = r'<!-- ATOC -->.*?<!-- ATOC -->'
        toc_match = re.search(toc_regex, content, re.DOTALL)

        # Initialiser les lignes du sommaire
        toc_lines = []

        # Si une section de sommaire existe déjà, on l'enlève
        if toc_match:
            content = content.replace(toc_match.group(), '')  # Supprimer l'ancien sommaire

        # Parcourir le contenu pour identifier les en-têtes
        lines = content.splitlines()
        for line in lines:
            if line.startswith('#'):
                level = line.count('#')  # Déterminer le niveau de l'en-tête
                title = line.strip('# ').strip()  # Enlever les # et les espaces
                if title.lower() != "sommaire":  # Exclure "Sommaire" du ToC
                    identifier = title.lower().replace(' ', '-').replace('é', 'e').replace('è', 'e')
                    toc_lines.append(f"{'  ' * (level - 1)}- [{title}](#{identifier})\n")

        # Créer le nouveau sommaire sans l'entrée "Sommaire"
        new_toc = "<!-- ATOC -->\n# Sommaire\n\n" + ''.join(toc_lines) + "\n<!-- ATOC -->"

        # Ajouter le nouveau sommaire en haut du fichier
        updated_content = new_toc + '\n' + content

        # Écrire le contenu mis à jour dans le fichier
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Sommaire mis à jour dans '{file_path}'.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    markdown_file = 'README.md'  # Remplacez par le chemin de votre fichier Markdown
    generate_markdown_toc(markdown_file)
