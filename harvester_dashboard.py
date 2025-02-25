import tkinter as tk
from network_scanner import scan_network

class HarvesterDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Seahawks Harvester Dashboard")

        # Affichage de l'IP locale
        self.ip_label = tk.Label(root, text="Adresse IP locale: 192.168.1.2")
        self.ip_label.pack()

        # Affichage du nombre de machines connectées
        self.machines_label = tk.Label(root, text="Machines connectées: 0")
        self.machines_label.pack()

        # Affichage de la latence
        self.latency_label = tk.Label(root, text="Latence moyenne: 30ms")
        self.latency_label.pack()

        # Bouton pour lancer un scan réseau
        self.scan_button = tk.Button(root, text="Lancer le scan réseau", command=self.run_scan)
        self.scan_button.pack()

        # Bouton pour mettre à jour le tableau de bord
        self.update_button = tk.Button(root, text="Mettre à jour", command=self.update_dashboard)
        self.update_button.pack()

    def run_scan(self):
        """
        Lance un scan réseau et met à jour les informations du tableau de bord.
        """
        target_network = '192.168.1.0/24'  # Vous pouvez changer cette adresse
        hosts = scan_network(target_network)
        self.machines_label.config(text=f"Machines connectées: {len(hosts)}")

    def update_dashboard(self):
        """
        Met à jour les informations du tableau de bord.
        """
        # Vous pouvez ajouter du code ici pour actualiser les autres données (latence, IP, etc.)
        print("Tableau de bord mis à jour.")

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = HarvesterDashboard(root)
    root.mainloop()
