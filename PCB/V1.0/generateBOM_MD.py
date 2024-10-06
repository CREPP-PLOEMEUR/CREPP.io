import csv

# Fonction pour lire la BOM à partir d'un fichier CSV de Kicad
def read_bom_from_kicad_csv(csv_file):
    # Créer des listes pour les résistances, LED, diodes et autres composants
    resistors = []
    leds = []
    diodes = []
    other_components = []

    # Ouvrir le fichier CSV et lire son contenu
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Utilisation de DictReader pour gérer les colonnes par nom
        
        # Lire chaque ligne du CSV (chaque ligne est un composant)
        for row in reader:
            ref = row['Référence']
            qty = row['Quantité']
            designation = row['Désignation'].lower()

            # Trier les composants selon leur type (résistance, LED, diode)
            if "résistance" in designation:
                value = add_resistor_unit(designation)  # Ajouter l'unité si c'est une résistance
                resistors.append((ref, qty, value))
            elif "led" in designation:
                leds.append((ref, qty, row['Désignation']))  # Ajouter les LED sans modification
            elif "diode" in designation:
                diodes.append((ref, qty, row['Désignation']))  # Ajouter les diodes sans modification
            else:
                other_components.append((ref, qty, row['Désignation']))

    # Retourner les composants avec les résistances en premier, suivies des LED, des diodes et des autres composants
    return resistors + leds + diodes + other_components

# Fonction pour ajouter une unité aux résistances si nécessaire
def add_resistor_unit(designation):
    value = designation.lower()

    if "k" in value:
        return value.replace("k", "kΩ")
    elif "m" in value:
        return value.replace("m", "MΩ")
    elif any(char.isdigit() for char in value):
        return value + " Ω" if "Ω" not in value else value
    return designation  # Si pas de changement nécessaire

# Fonction pour générer du markdown à partir des composants
def generate_markdown_bom(components):
    markdown = "# Bill of Materials (BOM)\n\n"
    markdown += "| Référence | Quantité | Désignation |\n"
    markdown += "|-----------|----------|-------------|\n"
    
    for ref, qty, designation in components:
        markdown += f"| {ref} | {qty} | {designation} |\n"
    
    return markdown

# Exemple d'utilisation
if __name__ == "__main__":
    # Chemin du fichier CSV de la BOM exportée de Kicad
    csv_file = 'bom/CREPP.io.csv'  # Remplacez par votre fichier CSV

    # Lire la BOM à partir du fichier CSV
    components = read_bom_from_kicad_csv(csv_file)

    # Générer le markdown
    markdown_output = generate_markdown_bom(components)

    # Afficher ou sauvegarder le markdown
    print(markdown_output)

    # Pour sauvegarder dans un fichier .md
    with open("BOM.md", "w") as md_file:
        md_file.write(markdown_output)
