import os
import pcbnew

def export_assembly_plans(input_pcb_path, output_dir):
    # Charger le fichier PCB
    board = pcbnew.LoadBoard(input_pcb_path)

    # Définir les fichiers PDF de sortie
    top_output_path = os.path.join(output_dir, "assembly_top.pdf")
    bottom_output_path = os.path.join(output_dir, "assembly_bottom.pdf")

    # Créer un objet PlotController pour gérer l'exportation
    plot_controller = pcbnew.PLOT_CONTROLLER(board)
    plot_options = plot_controller.GetPlotOptions()

    # Définir les options d'exportation pour PDF
    plot_options.SetOutputDirectory(output_dir)
    plot_options.SetPlotFrameRef(False)  # Désactiver le cadre de référence
    plot_options.SetLineWidth(pcbnew.FromMM(0.1))  # Définir la largeur des lignes
    plot_options.SetUseAuxOrigin(True)  # Utiliser l'origine auxiliaire si disponible
    plot_options.SetMirror(False)
    plot_options.SetScale(1)
    plot_options.SetPlotValue(True)  # Activer les valeurs de composants

    # Définir les couches à exporter (Silkscreen et Courtyard)
    layers_to_plot = [
        (pcbnew.F_SilkS, "Silkscreen Top"),
        (pcbnew.F_CrtYd, "Courtyard Top")
    ]

    # Exporter les couches pour la face du dessus
    plot_controller.SetLayer(pcbnew.F_SilkS)
    plot_controller.OpenPlotfile("top_silkscreen", pcbnew.PLOT_FORMAT_PDF, "Top Silkscreen")
    plot_controller.PlotLayer()

    plot_controller.SetLayer(pcbnew.F_CrtYd)
    plot_controller.OpenPlotfile("top_courtyard", pcbnew.PLOT_FORMAT_PDF, "Top Courtyard")
    plot_controller.PlotLayer()

    # Fusionner les fichiers pour le top
    os.system(f"pdftk {output_dir}/top_silkscreen.pdf {output_dir}/top_courtyard.pdf cat output {top_output_path}")

    # Exporter les couches pour la face du dessous
    plot_controller.SetLayer(pcbnew.B_SilkS)
    plot_controller.OpenPlotfile("bottom_silkscreen", pcbnew.PLOT_FORMAT_PDF, "Bottom Silkscreen")
    plot_controller.PlotLayer()

    plot_controller.SetLayer(pcbnew.B_CrtYd)
    plot_controller.OpenPlotfile("bottom_courtyard", pcbnew.PLOT_FORMAT_PDF, "Bottom Courtyard")
    plot_controller.PlotLayer()

    # Fusionner les fichiers pour le bottom
    os.system(f"pdftk {output_dir}/bottom_silkscreen.pdf {output_dir}/bottom_courtyard.pdf cat output {bottom_output_path}")

    print(f"Plans de montage générés avec succès : {top_output_path}, {bottom_output_path}")

# Exemple d'utilisation
input_pcb_path = "PCB/V1.0/CREPP.io.kicad_pcb"
output_dir = "plans_assemblage"
export_assembly_plans(input_pcb_path, output_dir)