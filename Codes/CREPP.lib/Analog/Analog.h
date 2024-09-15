#ifndef NETWORK_H
#define NETWORK_H

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

class Network 
{

    enum NetMode {
        WIFI_OFF,
        WIFI_ON
    };

public:
    Network();  

    
    void connectToRouter(const char* ssid, const char* password); // Connexion à un routeur Wi-Fi
    void startAccessPoint(const char* ssid, const char* password); // Démarrage en mode Point d'accès

    // Méthode pour récupérer l'adresse IP
    IPAddress getIPAddress();

    // Méthode pour configurer un serveur web et enregistrer une fonction de gestion HTML
    void startWebServer(void (*htmlCallback)());

private:
    void printWiFiStatus(); // Méthode privée pour afficher l'état du Wi-Fi

    ESP8266WebServer server;  // Serveur web intégré
    void (*htmlContentGenerator)();  // Pointeur de fonction pour générer le contenu HTML

    // Méthode privée pour gérer les requêtes HTTP
    void handleClientRequest();
};

#endif
