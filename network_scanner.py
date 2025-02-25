import nmap

def scan_network(target):
    """
    Scanne le réseau pour détecter les hôtes et les ports ouverts.
    :param target: Adresse IP ou plage d'adresses à scanner.
    :return: Liste des hôtes détectés.
    """
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-p 1-1024')  # Scanne les ports de 1 à 1024
    hosts = nm.all_hosts()
    return hosts

if __name__ == "__main__":
    # Exemple de scan d'un réseau local
    target_network = '192.168.1.0/24'
    hosts = scan_network(target_network)
    print(f"Machines détectées sur le réseau {target_network}: {hosts}")

