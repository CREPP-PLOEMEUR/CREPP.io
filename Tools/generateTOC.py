def generate_markdown_toc(file_path):
    try:
        # Ouvrir le fichier Markdown et lire son contenu
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        toc_lines = []  # Liste pour stocker les lignes du sommaire
        content_lines = []  # Liste pour stocker le reste du contenu
        toc_found = False  # Variable pour indiquer si un sommaire existe déjà

        # Parcourir les lignes et identifier les en-têtes
        for line in lines:
            if line.startswith('#'):
                # Vérifier si une ligne de sommaire est présente
                if line.strip() == "# Sommaire":
                    toc_found = True  # Un sommaire a été trouvé
                    toc_lines.append(line)  # Ajouter la ligne du sommaire au contenu
                    continue  # Passer à la ligne suivante

                # Déterminer le niveau de l'en-tête
                level = line.count('#')
                title = line.strip('# ').strip()  # Enlever le symbole # et les espaces
                # Créer l'identifiant de lien
                identifier = title.lower().replace(' ', '-').replace('é', 'e').replace('è', 'e')
                toc_lines.append(f"{'  ' * (level - 1)}- [{title}](#{identifier})\n")

            # Ajouter la ligne au contenu, qu'il s'agisse d'un en-tête ou non
            content_lines.append(line)

        # Si un sommaire n'a pas été trouvé, le créer
        if not toc_found:
            toc = "# Sommaire\n\n" + ''.join(toc_lines) + "\n"
            content_lines.insert(0, toc)  # Insérer le sommaire au début du contenu
        else:
            # Si le sommaire existe, le mettre à jour en enlevant l'ancien sommaire
            content_lines = [line for line in content_lines if line.strip() != "# Sommaire"]

            # Recréer le sommaire et le remettre
            toc = "# Sommaire\n\n" + ''.join(toc_lines) + "\n"
            content_lines.insert(0, toc)  # Insérer le sommaire mis à jour au début

        # Écrire le contenu mis à jour dans le même fichier
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(''.join(content_lines))

        print(f"Sommaire géré dans '{file_path}'.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    markdown_file = '../README.md'  # Remplacez par le chemin de votre fichier Markdown

    generate_markdown_toc(markdown_file)
